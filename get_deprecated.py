#!/usr/bin/env python3
import rdflib
from rdflib import Namespace
import sys

print(sys.argv[1])
print(sys.argv[2])
#yso = Namespace("http://www.yso.fi/onto/yso/")
#ysometa = Namespace("http://www.yso.fi/onto/yso-meta/2007-03-02/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
madsrdf = Namespace("http://www.loc.gov/mads/rdf/v1#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

i = 0
g = rdflib.Graph()
g_dest = rdflib.Graph()
# g.load('../../Finto-data/vocabularies/yso/ysoKehitys.rdf')
# g_dest.parse('./lcsh.both.nt', format="nt")
g.load(sys.argv[1])
g_dest.parse(sys.argv[2], format="nt")
list_of_failed_refs = open('list_of_broken_uris_new.txt', 'a')
list_of_deprecated_authorities = []

for s, p, o in g_dest.triples((None, rdf["type"], madsrdf["DeprecatedAuthority"])):
    list_of_deprecated_authorities.append(s)
    
for prop in [skos["closeMatch"], skos["broadMatch"], skos["narrowMatch"]]:
    for s, p, o in g.triples((None, prop, None)):
        if o in list_of_deprecated_authorities:
            i = i + 1
            list_of_failed_refs.write("{}: {} - {} - {}\n".format(i, s, p, o))
            print(str(i))
        
list_of_failed_refs.close()   
