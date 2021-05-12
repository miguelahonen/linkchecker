#!/usr/bin/env python3
import urllib3
import rdflib
from rdflib import Namespace
from rdflib.namespace import RDF
import time
import subprocess

skos = Namespace("http://www.w3.org/2004/02/skos/core#")
yso = Namespace("http://www.yso.fi/onto/yso/")
ysometa = Namespace("http://www.yso.fi/onto/yso-meta/2007-03-02/")
madsrdf = Namespace("http://www.loc.gov/mads/rdf/v1#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")


g = rdflib.Graph()
g.load('../../Finto-data/vocabularies/yso/ysoKehitys.rdf')
g_dest = rdflib.Graph()
g_dest.parse('./lcsh.both.nt', format="nt")
list_of_failed_refs = open('list_of_broken_uris_new.txt', 'a')
# g.load(sys.argv[1]) # RDF file will be read as command line argument
 	# madsrdf:DeprecatedAuthority

# ok
list_of_deprecated_authorities = []
for s, p, o in g_dest.triples((None, rdf["type"], madsrdf["DeprecatedAuthority"])):
    list_of_deprecated_authorities.append(s)
    
# skos:exactMatch skos:relatedMatch
i = 0
for prop in [skos["closeMatch"], skos["broadMatch"], skos["narrowMatch"]]:
    for s, p, o in g.triples((None, prop, None)):
        if o in list_of_deprecated_authorities:
            i = i + 1
            list_of_failed_refs.write("{}: {} - {} - {}\n".format(i, s, p, o))
            print(str(i))
        
list_of_failed_refs.close()   
        
        # if ((s, RDF.type, ysometa.Concept)) and not "x-preflabel" \
        #     in subprocess.getoutput("curl -I " + str(o + ".html").replace('http', 'https')):        

# for s, p, o in g_dest.triples((None, rdf["type"], madsrdf["DeprecatedAuthority"])):
#     print(str(s))
#     list_of_failed_refs.write("{}\n".format(s))



# for concept_and_skos_property, uri in dictOfMissedUrls.items():
#     list_of_failed_refs.write("{}: {}\n".format(concept_and_skos_property, uri))

# list_of_broken_uris_new.txt
# print(len(g_dest))
# import pprint
# for stmt in g_dest:
#     pprint.pprint(stmt)





# http = urllib3.PoolManager()
# dictOfMissedUrls = {}
# i = 0
# list_of_failed_refs = open('list_of_broken_uris.txt', 'a')


# for takenUri in :
    
#     10764440:<https://id.loc.gov/authorities/subjects/sh2010110119> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.loc.gov/mads/rdf/v1#DeprecatedAuthority> .

# # skos:exactMatch skos:relatedMatch
# for prop in [skos["closeMatch"], skos["broadMatch"], skos["narrowMatch"]]:
#     for s, p, o in g.triples((None, prop, None)):
#         if o in 
        
        
        
        
        
        
#         print(subprocess.getoutput("curl -I " + str(o + ".html").replace('http', 'https')))
#         if ((s, RDF.type, ysometa.Concept)) and not "x-preflabel" \
#             in subprocess.getoutput("curl -I " + str(o + ".html").replace('http', 'https')):
#             i = i + 1
#             print("* * * *")
#             print("Case: " + str(i))
#             # if "x-preflabel" in subprocess.getoutput("curl -I " + str(o + ".html").replace('http', 'https')):
#             #     print("..prefLabel found - the concept exists")
#             # if "x-preflabel" not in subprocess.getoutput("curl -I " + str(o + ".html").replace('http', 'https')):
#             print("We entered to the Area 51")
#             dictOfMissedUrls[s + ' : ' + p] = o
#             print("Case: {}".format(i))
#             print("Concept {} has a property {} ".format(s, p))
#             print("It refers to uri {}".format(o))
#             print("which does not existThe uri does not exist.")
#                 # else:
#                 #     print("Unexpected error")
                
# for concept_and_skos_property, uri in dictOfMissedUrls.items():
#     list_of_failed_refs.write("{}: {}\n".format(concept_and_skos_property, uri))

# list_of_failed_refs.close()



#
# Case: 2095
# Concept http://www.yso.fi/onto/yso/p27753 has a property http://www.w3.org/2004/02/skos/core#closeMatch
# and it refers to uri http://id.loc.gov/authorities/subjects/sh85084441.
# getting response 200. Related ysometa.Concept was added on the list






# for s, p, o in g.triples((None, skos.closeMatch, None)):
#     if ((s, RDF.type, ysometa.Concept)):
#         i = i + 1
#         r = http.request('GET', o)
#         if r.status != 200:
#             dictOfMissedUrls[s + ' : ' + p] = o
#             print("Case: {}".format(i))
#             print("Concept {} has a property skos.closeMatch".format(s))
#             print("and it refers to uri {}.".format(o))
#             print("The uri does not give a response 200 and the related ysometa.Concept was added on the list")
