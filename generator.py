import json
import os
import logging
import argparse
import re
import sys

import pysolr
import requests

import HTBookwormCatalogGenerator.util as u
import HTBookwormCatalogGenerator.classification as c
import HTBookwormCatalogGenerator.location as loc


#====================================
#FOR TESTING PURPOSES GETTING FILES FROM LOCAL DIRECTORY SINCE SERVICE ISN'T SET UP YET
#====================================
def _id_encode(id):
    '''
    :param id: A Pairtree ID. If it's a Hathitrust ID, this is the part after the library
        code; e.g. the part after the first period for vol.123/456.
    :return: A sanitized id. e.g., 123/456 will return as 123=456 to avoid filesystem issues.
    '''
    return id.replace(":", "+").replace("/", "=").replace(".", ",")

def clean_htid(htid):
    '''
    :param htid: A HathiTrust ID of form lib.vol; e.g. mdp.1234
    :return: A sanitized version of the HathiTrust ID, appropriate for filename use.
    '''
    libid, volid = htid.split('.', 1)
    volid_clean = _id_encode(volid)
    return '.'.join([libid, volid_clean])

def id_to_stubbytree(htid, format = None, suffix = None, compression = None):
    '''
    Take an HTRC id and convert it to a 'stubbytree' location.
    '''
    libid, volid = htid.split('.', 1)
    volid_clean = _id_encode(volid)

    suffixes = [s for s in [format, compression] if s is not None]
    filename = ".".join([clean_htid(htid), *suffixes])
    path = os.path.join(libid, volid_clean[::3], filename)
    return path

def id_to_rsync(htid, format="stubbytree"):
    '''
    Take an HTRC id and convert it to an Rsync location for syncing Extracted
    Features.
    '''
    if format == 'stubbytree':
        id_to_path_func = id_to_stubbytree
    elif format == "pairtree":
        id_to_path_func = id_to_pairtree
    else:
        raise ValueError("Unknown format for id_to_rsync")
    path = id_to_path_func(htid, format = "json", compression = "bz2")
    return path

def download_file(htids, outdir='./', keep_dirs=False, silent=True, format='stubbytree'):
    '''
    A function for downloading one or more Extracted Features files by ID.
    
    This uses a subprocess call to 'rsync', so will only work if rsync is available
    on your system and accessible in the same environment as Python.
    
    Returns (return code, stdout) tuple.
    
    htids:
        A string or list of strings, comprising HathiTrust identifiers.
        
    outdir:
        Location to save the file(s). Defaults to current directory.
        
    keep_dirs:
        Whether to keep the remote pairtree file structure or save just the files to outdir.
        Defaults to False (flattening).
        
    silent:
        If False, return the rsync stdout.
        
     
    Usage
    -------
    
    Download one file to the current directory:
    
    ```
    utils.download_file(htids='nyp.33433042068894')
    ```
    
    Download multiple files to the current directory:
    
    ```
    ids = ['nyp.33433042068894', 'nyp.33433074943592', 'nyp.33433074943600']
    utils.download_file(htids=ids)
    ```
    
    Download file to `/tmp`:
    ```
    utils.download_file(htids='nyp.33433042068894', outdir='/tmp')
    ```
    
    Download file to current directory, keeping pairtree directory structure;
    i.e. './nyp/pairtree_root/33/43/30/42/06/88/94/33433042068894/nyp.33433042068894.json.bz2':
    
    ```
    utils.download_file(htids='nyp.33433042068894', keep_dirs=True)
    ```
    
    '''
    import subprocess
    import tempfile
    import os
    import sys
    import bz2
    from six import string_types

    logging.debug(htids)

    tmppath = None
    sub_kwargs = dict()
    
    if not outdir.endswith("/"):
        outdir += "/"
    
    if keep_dirs:
        relative = '--relative'
    else:
        relative = '--no-relative'

    if isinstance(htids, string_types):
        # Download a single file
        dest_file = id_to_rsync(htids, format=format)
        args = ["queenpalm.ischool.illinois.edu::features-2020.03/" + dest_file]
    else:
        # Download a list of files
        paths = [id_to_rsync(htid, format=format) for htid in htids]
        
        fdescrip, tmppath =  tempfile.mkstemp()
        with open(tmppath, mode='w') as f:
            f.write("\n".join(paths))
        args = ["--files-from=%s" % tmppath, "queenpalm.ischool.illinois.edu::features-2020.03/"]

    cmd = ["rsync", relative, "-a","-v"] + args + [outdir]
    
    major, minor = sys.version_info[:2]
    if (major >= 3 and minor >=5):
        # Recommended use for 3.5+ is subprocess.run
        if not silent:
            sub_kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        else:
            devnull = open(os.devnull, 'w')
            sub_kwargs = dict(stdout=devnull, stderr=devnull, universal_newlines=True)

        response = subprocess.run(cmd, check=False, **sub_kwargs)
        if len(response.stderr) > 0:
            logging.debug("Error list:")
            logging.warning(response.stderr)
        out = (response.returncode, response.stdout)

    else:
        # Support older Python, currently without error catching
        out = (subprocess.call(cmd), None)
    
    if tmppath:
        f.close()
        os.close(fdescrip)
        os.remove(tmppath)

    output = b'['
    for htid in htids:
        logging.debug(outdir + '/' + htid.replace(':', "+").replace('/', "=") + '.json.bz2')
        try:
            file_object = bz2.open(outdir + '/' + htid.replace(':', "+").replace('/', "=") + '.json.bz2').read()
            output = output + file_object + b','
        except FileNotFoundError as e:
            logging.error(e)

    output = output[:-1] + b']'
    

    if len(output) > 1:    
        return output
    else:
        return b'[]'

#========================================


def main():
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("hathifile", nargs="?", help="location of HathiFile to parse", 
                        type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
    parser.add_argument("--outfile", nargs="?", help="Location to save output metadata. Bookworm wants jsoncatalog.txt, default is stdout.", 
                        type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument("--outDir", default=os.getcwd())
    parser.add_argument("--startLine", type=int, default = 0)
    parser.add_argument("--endLine", type=int, default = -1)
    parser.add_argument("--solrEndpoint", help="Which Solr endpoint should be queried for the API?",
        type=str, default = "http://data.htrc.illinois.edu/htrc-ef-access/get?action=download-ids&output=json")

    args = parser.parse_args()

    # Set up logger
    logging.basicConfig(filename=os.path.join(args.outDir, "solr2bookwormCat.log"),
                        filemode="a", level=logging.DEBUG) # Change to LOGGING.DEBUG for verbose msgs
    logging.info(args)

    # Set up PySolr
#    solr = pysolr.Solr(args.solrEndpoint, timeout=10)
    solr = args.solrEndpoint

    # Set defaults for output metadata record

    lineNum = 0
    volids = [] # list for collecting volume IDs to search in batches
    records = {}
    batch_size = 20
    could_not_find = []
    got_results_for = []
    # read in one line at a time, write out one json string at a time, logging progress
    for line in args.hathifile:
        logging.debug(line)
        lineNum+=1
        if lineNum < args.startLine:
            continue
        elif args.endLine > 0 and lineNum > args.endLine:
            break
        elif lineNum >= args.startLine:
            logging.debug("reading line number " + str(lineNum))
            row = (line.split('\t'))
            institutionId = (row[0].split('.'))[0]
            cleanVolumeId = row[0].replace(':', "+")
            cleanVolumeId = cleanVolumeId.replace('/', "=")

            # use volume id from hathifile
            volumeId = row[0]
            logging.debug("VolumeID: " + volumeId)
            volids += [volumeId]
            
            record = {"searchstring": "unknown", "lc_classes": [], "lc_subclass": [],
              "fiction_nonfiction": "unknown", "genres": [], "languages":[], "format": "unknown",
              "page_count_bin": "unknown", "word_count_bin": "unknown", 
              "publication_place": "unknown"}

            # Hathifile derived record info
            record['date'] = row[16]
            record['filename'] = cleanVolumeId
            record['publication_country'] = loc.marcCountryDict[row[17]] if row[17] in loc.marcCountryDict else "unknown"
            record['publication_state'] = loc.marcStateDict[row[17]] if row[17] in loc.marcStateDict else ""
            record['is_gov_doc'] = "Yes" if row[15] == 1 else "No"

            logging.debug(record)

            # Save record to records object, where we'll hold it until we query the Solr
            records[volumeId] = record

            # set default values in case a value is not available from solr
            #serial = "unknown"
            #genders =[]
            #publicationDate = 0

            logging.debug(len(volids))
            logging.debug(batch_size)

            if len(volids) >= batch_size:
                found_volids = {}
                for volid in volids:
                    found_volids[volid] = False

                logging.info("%d records collected, Querying solr now." % batch_size)
                results = download_file(volids,outdir='ef2_files',silent=False)
#                results = querySolr(volids, solr, batch_size)
#                logging.debug(results)
                results_content = json.loads(results.decode())
                for result in results_content:
                    #remove the processed file to preserve disk space
                    os.remove('ef2_files/' + result['htid'].replace(':', "+").replace('/', "=") + '.json.bz2')
                    got_results_for.append(result['htid'])
#                    logging.debug("Got results for: " + result['htid'])
#                    logging.debug(records.keys())
                    found_volids[result['htid']] = True
                    htfile_record = records[result['htid']]
                    record = build_record(result['htid'], result, htfile_record)
                    args.outfile.write(json.dumps(record)+'\n')

                for element in found_volids:
                    if not found_volids[element]:
                        could_not_find.append(element)
#                        logging.debug("Could not find " + element)

                volids = []
                records = {}
#    sys.exit()
    # Process any outstanding files
    found_volids = {}
    for volid in volids:
        found_volids[volid] = False
    logging.info("%d records collected, Querying solr now." % len(volids))
    results = download_file(volids,outdir='ef2_files',silent=False)
#    results = querySolr(volids, solr, batch_size)
#    logging.debug(results)
    results_content = json.loads(results.decode())
    for result in results_content:
        #remove the processed file to preserve disk space
        os.remove('ef2_files/' + result['htid'].replace(':', "+").replace('/', "=") + '.json.bz2')
        got_results_for.append(result['htid'])
#        logging.debug("Got results for: " + result['htid'])
#        logging.debug(records.keys())
        found_volids[result['htid']] = True
        htfile_record = records[result['htid']]
        record = build_record(result['htid'], result, htfile_record)
        args.outfile.write(json.dumps(record)+'\n')

    for element in found_volids:
        if not found_volids[element]:
            could_not_find.append(element)
#            logging.debug("Could not find " + element)

    logging.debug("Got results for %d records:" % len(got_results_for))
    for res in got_results_for:
        logging.debug(res)

    logging.debug("Could not find results for %d records:" % len(could_not_find))
    for nres in could_not_find:
        logging.debug(nres)

    logging.info("done")

def querySolr(volids, solr, rows):
    ''' Queries multiple solr ids at once. Returns empty list when there are no results.'''
    if len(volids) == 0:
        return []

    # Make volume ids into query string
    q = solr + "&ids=%s" % ",".join(volids)
    logging.debug(q)

    # get information from Solr
    try:
#        results = solr.search(q, rows=rows)
        results = requests.get(q)
    except Exception:
        logging.exception("Problem with search for \"%s\"" % q)
        return []
#    logging.debug(list(results))

    if results.headers['Content-Type'] != 'application/json;charset=utf-8':
        return []
    return results 
    

def build_record(volumeId, result, record):
    ''' 
    Process Solr API results
    results : JSON object of results from Solr
    records : object of HATHI derived record information, to augment with Solr info and
              write to jsoncatalog.txt
    '''
    logging.debug(record)

    if 'pubDate' in result['metadata']:
        try:
            record['date'] = int(result['metadata']['pubDate'])
        except (ValueError, TypeError) as e:
            pass

    if "lcc" in result['metadata']:
        for callNumber in result['metadata']['lcc']:
            classResponse = c.getClass(callNumber)
            if classResponse is not None:
                record['lc_classes'].append(c.getClass(callNumber))

            subclassResponse = c.getSubclass(callNumber)
            if subclassResponse is not None:
                record['lc_subclass'].append(c.getSubclass(callNumber))

    if "genre" in result['metadata']:
        if type(result['metadata']['genre']) is str:
            record['genres'].append(result['metadata']['genre'])
        else:
            for genre in result['metadata']['genre']:
                if genre == 'http://id.loc.gov/vocabulary/marcgt/fic':
                    record['fiction_nonfiction'] = 'Fiction'
#                elif genre == 'Not fiction':
#                    record['fiction_nonfiction'] = 'Not fiction'
                else:
                    record['genres'].append(genre)

#    if "typeOfResource" in result['metadata']:
#        record["format"] = result['metadata']["typeOfResource"]

#    for key in ["format", "publication_place"]:
#        # Doublecheck that solr returned the field
#        if key in result:
#            record[key] = result[key][0]

    if "language" in result['metadata']:
        if type(result['metadata']["language"]) is list:
            record['languages'] = result['metadata']["language"] # Use the full list
        else:
            record['languages'] = [ result['metadata']["language"] ]

 
    if "title" in result['metadata']:
        title = result['metadata']['title']
    else:
        title = "unknown"

    if "pubPlace" in result['metadata']:
        if type(result['metadata']["pubPlace"]) is list:
            if 'name' in result['metadata']["pubPlace"][0]:
                record["publication_place"] = result['metadata']["pubPlace"][0]["name"]
        else:
            if 'name' in result['metadata']["pubPlace"]:
                record["publication_place"] = result['metadata']["pubPlace"]["name"]

    if 'pubPlace' in result['metadata'] and record['publication_country'] == "unknown":
        if type(result['metadata']["pubPlace"]) is list:
            country_code = result['metadata']['pubPlace'][0]['id'][:-result['metadata']['pubPlace'][0]['id'].rfind('/')]
        else:
            country_code = result['metadata']['pubPlace']['id'][:-result['metadata']['pubPlace']['id'].rfind('/')]

        logging.debug(country_code)
        record['publication_country'] = loc.marcCountryDict[country_code] if country_code in loc.marcCountryDict else "unknown"

    if 'pageCount' in result['features']:
        record['page_count_bin'] = u.getPageBin(int(result['features']['pageCount']))
    
    if 'pages' in result['features']:
        record['word_count_bin'] = u.getWordBin(int(sum([ page['tokenCount'] for page in result['features']['pages'] ])))

    
    multi_fields = ["htrc_gender"]

    if 'sourceInstitution' in result['metadata']:
        record['htsource'] = [ result['metadata']['sourceInstitution']['name'] ]

    try:
        if type(result['metadata']['contributor']) is list:
            record['mainauthor'] = [ instance['name'] for instance in result['metadata']['contributor'] ]
        else:
            record['mainauthor'] = [ result['metadata']['contributor']['name'] ]
    except KeyError:
        record['mainauthor'] = []

    try:
        if type(result['metadata']['publisher']) is list:
            record['publisher'] = [ instance['name'] for instance in result['metadata']['publisher'] ]
        else:
            record['publisher'] = [ result['metadata']['publisher']['name'] ]
    except KeyError:
        record['publisher'] = []

    record['format'] = [ result['metadata']['type'][1] ]

    try:
        record['format'].append(result['metadata']['typeOfResource'])
    except KeyError:
        pass

    record['htrc_gender'] = []

    for field in ['lc_classes', 'lc_subclass', 'genres', 'languages', 'htsource', 'mainauthor', 'publisher', 'format', 'htrc_gender']:
        # eliminate duplicates
        record[field] = list(set(record[field]))
        # add unknown value to empty arrays so they can be searched using filters
        if len(record[field]) == 0:
            record[field] = ['unknown']

    record['searchstring'] = "<a href='http://hdl.handle.net/2027/%s'>%s</a>" % (volumeId, title)


    return record

if __name__ == '__main__':
    main()
