
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify

import pickle
import json

import rdflib
from math import *
from rdflib import Namespace
import sys
from operator import itemgetter

def CityWeather(city,type):
    response = []
    ToHtml = ""
    ToJs = ""
    g = rdflib.Graph()
    g.namespace_manager.bind('ns', Namespace('http://www.semanticweb.org/admin/ontologies/2022/2/untitled-ontology-30#'))
    g.namespace_manager.bind('rdf', Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'))
    g.namespace_manager.bind('rdfs', Namespace('http://www.w3.org/2000/01/rdf-schema#'))
    g.namespace_manager.bind('owl', Namespace('http://www.w3.org/2002/07/owl#'))
    g.namespace_manager.bind('xsd', Namespace('http://www.w3.org/2001/XMLSchema#'))
    g.parse("final_ontology.owl")
    query = "SELECT DISTINCT ?name ?lon ?lat WHERE { ?target ns:city ?city . ?target ns:city \""+city+"\" . ?target ns:longitude ?lon . ?target ns:latitude ?lat. }"
    print("helllo")
    print(query)
    #query = "SELECT ?x WHERE { ?x ns:city \"Paris\".}"
    #query = "SELECT ?name ?lat ?lon WHERE { ?name ns:city \"Paris\" . ?name ns:longitude ?lon. ?name ns:latitude ?lat. }"

    res = g.query(query)
    print("hmm")
    print(res)
    for elmt in res:
        element =  elmt.asdict()
        print(element)
        input()
        for key in element:
            element[key] = element[key].toPython()
        response.append(element)
    lat,lon = response[0]['lat'],response[0]['lon']
    response = []
    if type == "Weather":
        query = "SELECT DISTINCT ?name ?lon ?lat WHERE { ?target ns:city ?city . ?target ns:city \""+city+"\". ?target ns:longitude ?lon . ?target ns:latitude ?lat. }"
        #query = "SELECT DISTINCT ?des ?hum ?temp WHERE { ?target ns:city ?Weather . ?target ns:city \""+city+"\" . ?target ns:description ?des . ?target ns:humidity ?hum . ?target ns:temp ?temp. }"
        res = g.query(query)
        for elmt in res:
            element =  elmt.asdict()
            for key in element:
                element[key] = element[key].toPython()
            response.append(element)
            print(element)
            input()


CityWeather("Paris","Weather")
