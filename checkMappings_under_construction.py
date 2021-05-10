#!/usr/bin/env python3
import urllib3
import rdflib
from rdflib import Namespace
from rdflib.namespace import RDF
import time

skos = Namespace("http://www.w3.org/2004/02/skos/core#")
yso = Namespace("http://www.yso.fi/onto/yso/")
ysometa = Namespace("http://www.yso.fi/onto/yso-meta/2007-03-02/")
g = rdflib.Graph()
# g.load(sys.argv[1]) # RDF file will be read as command line argument
g.load('../../Finto-data/vocabularies/yso/ysoKehitys.rdf')

http = urllib3.PoolManager()
dictOfMissedUrls = {}
i = 0
list_of_failed_refs = open('list_of_broken_uris.txt', 'a')

# skos:exactMatch skos:relatedMatch
for prop in [skos["closeMatch"], skos["broadMatch"], skos["narrowMatch"]]:
    for s, p, o in g.triples((None, prop, None)):
        if ((s, RDF.type, ysometa.Concept)):
            i = i + 1
            print("***")
            print(str(prop))
            print(str(i))
            print("***")
            r = http.request('GET', o)
            time.sleep(1)
            if r.status != 200:
                dictOfMissedUrls[s + ' : ' + p] = o
                print("Case: {}".format(i))
                print("Concept {} has a property {} ".format(s, p))
                print("It refers to uri {}".format(o))
                print("and fails to get response 200. Related ysometa.Concept was added on the list")

for concept_and_skos_property, uri in dictOfMissedUrls.items():
    list_of_failed_refs.write("{}: {}\n".format(concept_and_skos_property, uri))

list_of_failed_refs.close()



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
