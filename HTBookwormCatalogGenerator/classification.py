# Based on Library of Congress Classification http://www.loc.gov/catdir/cpso/lcco/
classDict = {}
classDict['A'] = "General Works"
classDict['B'] = "Philosophy, Psychology, and Religion"
classDict['C'] = "Auxiliary Sciences of History"
classDict['D'] = "General and Old World History"
classDict['E'] = "History of America"
classDict['F'] = "History of the United States and British, Dutch, French, and Latin America"
classDict['G'] = "Geography, Anthropology, and Recreation"
classDict['H'] = "Social Sciences"
classDict['J'] = "Political Science"
classDict['K'] = "Law"
classDict['L'] = "Education"
classDict['M'] = "Music"
classDict['N'] = "Fine Arts"
classDict['P'] = "Language and Literature"
classDict['Q'] = "Science"
classDict['R'] = "Medicine"
classDict['S'] = "Agriculture"
classDict['T'] = "Technology"
classDict['U'] = "Military Science"
classDict['V'] = "Naval Science"
classDict['Z'] = "Bibliography, Library Science, and General Information Resources"

subClass3charDict = {}
subClass3charDict['DAW'] = "Central Europe"
subClass3charDict['DJK'] = "Eastern Europe (General)"
subClass3charDict['KBM'] = "Jewish law"
subClass3charDict['KBP'] = "Islamic law"
subClass3charDict['KBR'] = "History of canon law"
subClass3charDict['KBS'] = "Canon law of Eastern churches"
subClass3charDict['KBT'] = "Canon law of Eastern Rite Churches in Communion with the Holy See of Rome"
subClass3charDict['KBU'] = "Law of the Roman Catholic Church. The Holy See"
subClass3charDict['KDK'] = "United Kingdom and Ireland"
subClass3charDict['KDZ'] = "America. North America"
subClass3charDict['KKZ'] = "Europe"
subClass3charDict['KWX'] = "Asia and Eurasia, Africa, Pacific Area, and Antarctica"
# special case -- not real subclass, but common cataloging error
subClass3charDict['LAW'] = "Law"

subClass2charDict = {}
subClass2charDict['AC'] = "Collections. Series. Collected works"
subClass2charDict['AE'] = "Encyclopedias"
subClass2charDict['AG'] = "Dictionaries and other general reference works"
subClass2charDict['AI'] = "Indexes"
subClass2charDict['AM'] = "Museums. Collectors and collecting"
subClass2charDict['AN'] = "Newspapers"
subClass2charDict['AP'] = "Periodicals"
subClass2charDict['AS'] = "Academies and learned societies"
subClass2charDict['AY'] = "Yearbooks. Almanacs. Directories"
subClass2charDict['AZ'] = "History of scholarship and learning. The humanities"
subClass2charDict['BC'] = "Logic"
subClass2charDict['BD'] = "Speculative philosophy"
subClass2charDict['BF'] = "Psychology"
subClass2charDict['BH'] = "Aesthetics"
subClass2charDict['BJ'] = "Ethics"
subClass2charDict['BL'] = "Religions. Mythology. Rationalism"
subClass2charDict['BM'] = "Judaism"
subClass2charDict['BP'] = "Islam. Bahaism. Theosophy, etc."
subClass2charDict['BQ'] = "Buddhism"
subClass2charDict['BR'] = "Christianity"
subClass2charDict['BS'] = "The Bible"
subClass2charDict['BT'] = "Doctrinal Theology"
subClass2charDict['BV'] = "Practical Theology"
subClass2charDict['BX'] = "Christian Denominations"
subClass2charDict['CB'] = "History of Civilization"
subClass2charDict['CC'] = "Archaeology"
subClass2charDict['CD'] = "Diplomatics. Archives. Seals"
subClass2charDict['CE'] = "Technical Chronology. Calendar"
subClass2charDict['CJ'] = "Numismatics"
subClass2charDict['CN'] = "Inscriptions. Epigraphy"
subClass2charDict['CR'] = "Heraldry"
subClass2charDict['CS'] = "Genealogy"
subClass2charDict['CT'] = "Biography"
subClass2charDict['DA'] = "Great Britain"
subClass2charDict['DB'] = "Austria Liechtenstein Hungary Czechoslovakia"
subClass2charDict['DC'] = "France Andorra Monaco"
subClass2charDict['DD'] = "Germany"
subClass2charDict['DE'] = "Greco-Roman World"
subClass2charDict['DF'] = "Greece"
subClass2charDict['DG'] = "Italy Malta"
subClass2charDict['DH'] = "Low Countries Benelux Countries"
subClass2charDict['DJ'] = "Netherlands (Holland)"
subClass2charDict['DK'] = "Russia. Soviet Union. Former Soviet Republics Poland"
subClass2charDict['DL'] = "Northern Europe. Scandinavia"
subClass2charDict['DP'] = "Spain Portugal"
subClass2charDict['DQ'] = "Switzerland"
subClass2charDict['DR'] = "Balkan Peninsula"
subClass2charDict['DS'] = "Asia"
subClass2charDict['DT'] = "Africa"
subClass2charDict['DU'] = "Oceania (South Seas)"
subClass2charDict['DX'] = "Gypsies"
subClass2charDict['GA'] = "Mathematical geography. Cartography"
subClass2charDict['GB'] = "Physical geography"
subClass2charDict['GC'] = "Oceanography"
subClass2charDict['GE'] = "Environmental Sciences"
subClass2charDict['GF'] = "Human ecology. Anthropogeography"
subClass2charDict['GN'] = "Anthropology"
subClass2charDict['GR'] = "Folklore"
subClass2charDict['GT'] = "Manners and customs (General)"
subClass2charDict['GV'] = "Recreation. Leisure"
subClass2charDict['HA'] = "Statistics"
subClass2charDict['HB'] = "Economic theory. Demography"
subClass2charDict['HC'] = "Economic history and conditions"
subClass2charDict['HD'] = "Industries. Land use. Labor"
subClass2charDict['HE'] = "Transportation and communications"
subClass2charDict['HF'] = "Commerce"
subClass2charDict['HG'] = "Finance"
subClass2charDict['HJ'] = "Public finance"
subClass2charDict['HM'] = "Sociology (General)"
subClass2charDict['HN'] = "Social history and conditions. Social problems. Social reform"
subClass2charDict['HQ'] = "The family. Marriage. Women"
subClass2charDict['HS'] = "Societies: secret, benevolent, etc."
subClass2charDict['HT'] = "Communities. Classes. Races"
subClass2charDict['HV'] = "Social pathology. Social and public welfare. Criminology"
subClass2charDict['HX'] = "Socialism. Communism. Anarchism"
subClass2charDict['JA'] = "Political science (General)"
subClass2charDict['JC'] = "Political theory"
subClass2charDict['JF'] = "Political institutions and public administration"
subClass2charDict['JJ'] = "Political institutions and public administration (North America)"
subClass2charDict['JK'] = "Political institutions and public administration (United States)"
subClass2charDict['JL'] = "Political institutions and public administration (Canada, Latin America, etc.)"
subClass2charDict['JN'] = "Political institutions and public administration (Europe)"
subClass2charDict['JQ'] = "Political institutions and public administration (Asia, Africa, Australia, Pacific Area, etc.)"
subClass2charDict['JS'] = "Local government. Municipal government"
subClass2charDict['JV'] = "Colonies and colonization. Emigration and immigration. International migration"
subClass2charDict['JX'] = "International law, see JZ and KZ (obsolete)"
subClass2charDict['JZ'] = "International relations"
subClass2charDict['KB'] = "Religious law in general. Comparative religious law. Jurisprudence"
subClass2charDict['KD'] = "United Kingdom and Ireland"
subClass2charDict['KE'] = "Canada"
subClass2charDict['KF'] = "United States"
subClass2charDict['KG'] = "Latin America Mexico and Central America West Indies. Caribbean area"
subClass2charDict['KH'] = "South America"
subClass2charDict['KJ'] = "Europe"
subClass2charDict['KK'] = "Europe"
subClass2charDict['KL'] = "Asia and Eurasia, Africa, Pacific Area, and Antarctica"
subClass2charDict['KW'] = "Asia and Eurasia, Africa, Pacific Area, and Antarctica"
subClass2charDict['KZ'] = "Law of nations"
subClass2charDict['LA'] = "History of education"
subClass2charDict['LB'] = "Theory and practice of education"
subClass2charDict['LC'] = "Special aspects of education"
subClass2charDict['LD'] = "Individual institutions United States"
subClass2charDict['LE'] = "Individual institutions America (except United States)"
subClass2charDict['LF'] = "Individual institutions Europe"
subClass2charDict['LG'] = "Individual institutions Asia, Africa, Indian Ocean islands, Australia, New Zealand, Pacific islands"
subClass2charDict['LH'] = "College and school magazines and papers"
subClass2charDict['LJ'] = "Student fraternities and societies, United States"
subClass2charDict['LT'] = "Textbooks"
subClass2charDict['ML'] = "Literature on music"
subClass2charDict['MT'] = "Instruction and study"
subClass2charDict['NA'] = "Architecture"
subClass2charDict['NB'] = "Sculpture"
subClass2charDict['NC'] = "Drawing. Design. Illustration"
subClass2charDict['ND'] = "Painting"
subClass2charDict['NE'] = "Print media"
subClass2charDict['NK'] = "Decorative arts"
subClass2charDict['NX'] = "Arts in general"
subClass2charDict['PA'] = "Greek language and literature. Latin language and literature"
subClass2charDict['PB'] = "Modern languages. Celtic languages"
subClass2charDict['PC'] = "Romanic languages"
subClass2charDict['PD'] = "Germanic languages. Scandinavian languages"
subClass2charDict['PE'] = "English language"
subClass2charDict['PF'] = "West Germanic languages"
subClass2charDict['PG'] = "Slavic languages and literatures. Baltic languages. Albanian language"
subClass2charDict['PH'] = "Uralic languages. Basque language"
subClass2charDict['PJ'] = "Oriental languages and literatures"
subClass2charDict['PK'] = "Indo-Iranian languages and literatures"
subClass2charDict['PL'] = "Languages and literatures of Eastern Asia, Africa, Oceania"
subClass2charDict['PM'] = "Hyperborean, Native American, and artificial languages"
subClass2charDict['PN'] = "Literature (General)"
subClass2charDict['PQ'] = "French literature Italian literature Spanish literature Portuguese literature"
subClass2charDict['PR'] = "English literature"
subClass2charDict['PS'] = "American literature"
subClass2charDict['PT'] = "Germanic literature"
subClass2charDict['PZ'] = "Fiction and juvenile belles lettres"
subClass2charDict['QA'] = "Mathematics"
subClass2charDict['QB'] = "Astronomy"
subClass2charDict['QC'] = "Physics"
subClass2charDict['QD'] = "Chemistry"
subClass2charDict['QE'] = "Geology"
subClass2charDict['QH'] = "Natural history Biology"
subClass2charDict['QK'] = "Botany"
subClass2charDict['QL'] = "Zoology"
subClass2charDict['QM'] = "Human anatomy"
subClass2charDict['QP'] = "Physiology"
subClass2charDict['QR'] = "Microbiology"
subClass2charDict['RA'] = "Public aspects of medicine"
subClass2charDict['RB'] = "Pathology"
subClass2charDict['RC'] = "Internal medicine"
subClass2charDict['RD'] = "Surgery"
subClass2charDict['RE'] = "Ophthalmology"
subClass2charDict['RF'] = "Otorhinolaryngology"
subClass2charDict['RG'] = "Gynecology and Obstetrics"
subClass2charDict['RJ'] = "Pediatrics"
subClass2charDict['RK'] = "Dentistry"
subClass2charDict['RL'] = "Dermatology"
subClass2charDict['RM'] = "Therapeutics. Pharmacology"
subClass2charDict['RS'] = "Pharmacy and materia medica"
subClass2charDict['RT'] = "Nursing"
subClass2charDict['RV'] = "Botanic, Thomsonian, and Eclectic medicine"
subClass2charDict['RX'] = "Homeopathy"
subClass2charDict['RZ'] = "Other systems of medicine"
subClass2charDict['SB'] = "Horticulture. Plant propagation. Plant breeding"
subClass2charDict['SD'] = "Forestry. Arboriculture. Silviculture"
subClass2charDict['SF'] = "Animal husbandry. Animal science"
subClass2charDict['SH'] = "Aquaculture. Fisheries. Angling"
subClass2charDict['SK'] = "Hunting"
subClass2charDict['TA'] = "Engineering Civil engineering (General)"
subClass2charDict['TC'] = "Hydraulic engineering. Ocean engineering"
subClass2charDict['TD'] = "Environmental technology. Sanitary engineering"
subClass2charDict['TE'] = "Highway engineering. Roads and pavements"
subClass2charDict['TF'] = "Railroad engineering and operation"
subClass2charDict['TG'] = "Bridges"
subClass2charDict['TH'] = "Building construction"
subClass2charDict['TJ'] = "Mechanical engineering and machinery"
subClass2charDict['TK'] = "Electrical engineering. Electronics. Nuclear engineering"
subClass2charDict['TL'] = "Motor vehicles. Aeronautics. Astronautics"
subClass2charDict['TN'] = "Mining engineering. Metallurgy"
subClass2charDict['TP'] = "Chemical technology"
subClass2charDict['TR'] = "Photography"
subClass2charDict['TS'] = "Manufacturing engineering. Mass production"
subClass2charDict['TT'] = "Handicrafts. Arts and crafts"
subClass2charDict['TX'] = "Home economics"
subClass2charDict['UA'] = "Armies: Organization, distribution, military situation"
subClass2charDict['UB'] = "Military administration"
subClass2charDict['UC'] = "Military maintenance and transportation"
subClass2charDict['UD'] = "Infantry"
subClass2charDict['UE'] = "Cavalry. Armor"
subClass2charDict['UF'] = "Artillery"
subClass2charDict['UG'] = "Military engineering. Air forces"
subClass2charDict['UH'] = "Other military services"
subClass2charDict['VA'] = "Navies: Organization, distribution, naval situation"
subClass2charDict['VB'] = "Naval administration"
subClass2charDict['VC'] = "Naval maintenance"
subClass2charDict['VD'] = "Naval seamen"
subClass2charDict['VE'] = "Marines"
subClass2charDict['VF'] = "Naval ordnance"
subClass2charDict['VG'] = "Minor services of navies"
subClass2charDict['VK'] = "Navigation. Merchant marine"
subClass2charDict['VM'] = "Naval architecture. Shipbuilding. Marine engineering"
subClass2charDict['ZA'] = "Information resources (General)"

subClass1charDict = {}
subClass1charDict['B'] = "Philosophy (General)"
subClass1charDict['C'] = "Auxiliary Sciences of History (General)"
subClass1charDict['D'] = "History (General)"
subClass1charDict['G'] = "Geography (General)"
subClass1charDict['H'] = "Social sciences (General)"
subClass1charDict['J'] = "General legislative and executive papers"
subClass1charDict['K'] = "Law in general. Comparative and uniform law. Jurisprudence"
subClass1charDict['L'] = "Education (General)"
subClass1charDict['M'] = "Music"
subClass1charDict['N'] = "Visual arts"
subClass1charDict['P'] = "Philology. Linguistics"
subClass1charDict['Q'] = "Science (General)"
subClass1charDict['R'] = "Medicine (General)"
subClass1charDict['S'] = "Agriculture (General)"
subClass1charDict['T'] = "Technology (General)"
subClass1charDict['U'] = "Military science (General)"
subClass1charDict['V'] = "Naval science (General)"
subClass1charDict['Z'] = "Books (General). Writing. Paleography"

def getClass(callNumber):
    if callNumber[:3].lower() == "law":
        return classDict['K']
    elif callNumber[:1] in classDict:
        return classDict[callNumber[:1].upper()]
    else:
        return None

def getSubclass(callNumber):

    if callNumber[:3] in subClass3charDict:
        return subClass3charDict[callNumber[:3].upper()]
    elif callNumber[:2] in subClass2charDict:
        return subClass2charDict[callNumber[:2].upper()]
    elif callNumber[:1] in subClass1charDict:
        return subClass1charDict[callNumber[:1].upper()]
    else:
        return None
