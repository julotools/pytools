import json
import os
import zlib
from os import walk
import argparse

def convert_zlib(cin,cout):
    for (repertoire, sousRepertoires, l_fichiers) in walk(cin):
        for f in l_fichiers:
            with open(cin+f, "rb") as handle:
                data = zlib.decompress(handle.read())
                f = open(cout+f+"_r.json", "a")	
                f.write(str(json.loads(data)))
                f.close()
                print(" -> "+cout+"result.json")
    print("done")

#gestion des argument
parser = argparse.ArgumentParser(description="convert zlib file to json\nex : python3 zlib2json.py -i nom_dossier_contenant_les_zlib -o dossier_result")
parser.add_argument("-i", "--input", type=str, 
                    help="chemin du dossier d'entrée")
parser.add_argument("-o", "--output", type=str, 
                    help="chemin du dossier de sortie")

args = parser.parse_args()

chemin_in = "."
if args.input:
    chemin_in=args.input
chemin_out = "."
if args.output:
    chemin_out=args.output
if chemin_in[-1]!='/':
    chemin_in+='/'
if chemin_out[-1]!='/':
    chemin_out+='/'

convert_zlib(chemin_in,chemin_out)
