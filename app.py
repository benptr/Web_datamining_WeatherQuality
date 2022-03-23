# Importing libraries

from flask import Flask, request, render_template, redirect, url_for, flash, jsonify

import pickle
import json

import rdflib
from math import *
from rdflib import Namespace
import sys
from operator import itemgetter


# Creating data manipulation functions
def CityPosition():
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
    
    query = "SELECT DISTINCT ?name ?lon ?lat WHERE { ?target ns:city ?city . ?target ns:city ?name. ?target ns:longitude ?lon . ?target ns:latitude ?lat. } ORDER BY ?name"
    res = g.query(query)
    for elmt in res:
            element =  elmt.asdict()
            for key in element:
                element[key] = element[key].toPython()
            response.append(element)
    response = response[:100]
    for i in range(len(response)):
        print(response[i]['name'],response[i]['lat'],response[i]['lon'])
        ToHtml += "<li><b>" + str(response[i]['name']) + "</b> — lat: "  + str(response[i]['lat']) + "; lon: " + str(response[i]['lon']) +"</li>"
        ToJs += "L.marker([" + str(response[i]['lat']) + ", " + str(response[i]['lon']) + "]).addTo(mymap).bindPopup('City<br><b>" + str(response[i]['name']) + "</b><br>lat. " + str(response[i]['lat']) + "; lon: " + str(response[i]['lon']) + "');\n"
    return (ToHtml, ToJs)


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
    query = "SELECT DISTINCT ?name ?lon ?lat WHERE { ?target ns:city ?city . ?target ns:city ?name. ?target ns:longitude ?lon . ?target ns:latitude ?lat. } ORDER BY ?name"
    res = g.query(query)
    lat,lon = 0,0
    for elmt in res:
        element =  elmt.asdict()
        for key in element:
            element[key] = element[key].toPython()
        if element['name'] == city:
            lat,lon =element['lat'],element['lon']
    print(lat,lon)

    if type == "Weather":
        query = "SELECT DISTINCT ?name ?des ?temp ?min ?max ?hum WHERE { ?target ns:city ?Weather. ?target ns:city ?name. ?target ns:description ?des. ?target ns:temp ?temp. ?target ns:temp_min ?min. ?target ns:temp_max ?max. ?target ns:humidity ?hum. }"
        res = g.query(query)
        for elmt in res:
            element =  elmt.asdict()
            for key in element:
                element[key] = element[key].toPython()
            if element['name'] == city:
                response.append(element)
        print(response)
        for i in range(len(response)):
            ToHtml += "<li><b>" + str(response[i]['name']) + "</b> — description: "  + str(response[i]['des']) + "; temperature: " + str(response[i]['temp']) +"; min: " + str(response[i]['min']) +"; max: " + str(response[i]['max']) +"; humidity: " + str(response[i]['hum']) +"</li>"
            ToJs += "L.marker([" + str(lat) + ", " + str(lon) + "]).addTo(mymap).bindPopup('City<br><b>" + str(response[i]['name']) + "</b><br>description: "  + str(response[i]['des']) + "; temperature: " + str(response[i]['temp']) +"; min: " + str(response[i]['min']) +"; max: " + str(response[i]['max']) +"; humidity: " + str(response[i]['hum']) + "');\n"
        return (ToHtml, ToJs,lat,lon)
    elif type == "Air_Pollution":
        
        query = "SELECT DISTINCT ?name ?o3a ?o3p ?aqi WHERE { ?target ns:city ?Airquf. ?target ns:city ?name. ?target ns:aqi ?aqi. ?target ns:today_o3_average ?o3a. ?target ns:tomorrow_o3_average ?o3p.}"
        res = g.query(query)
        for elmt in res:
            element =  elmt.asdict()
            for key in element:
                element[key] = element[key].toPython()
            if element['name'] == city:
                response.append(element)
        print(response)
        for i in range(len(response)):
            ToHtml += "<li><b>" + str(response[i]['name']) + "</b> — o3 today: "  + str(response[i]['o3a']) + "; o3 tomorrow: " + str(response[i]['o3p']) +"; aqi: " + str(response[i]['aqi']) +"</li>"
            ToJs += "L.marker([" + str(lat) + ", " + str(lon) + "]).addTo(mymap).bindPopup('City<br><b>" + str(response[i]['name']) + "</b><br>o3 today: "  + str(response[i]['o3a']) + "; o3 tomorrow: " + str(response[i]['o3p']) +"; aqi: " + str(response[i]['aqi']) + "');\n"
        return (ToHtml, ToJs,lat,lon)
    else:
        query = "SELECT DISTINCT ?name ?des ?temp ?min ?max ?hum WHERE { ?target ns:city ?Weather. ?target ns:city ?name. ?target ns:description ?des. ?target ns:temp ?temp. ?target ns:temp_min ?min. ?target ns:temp_max ?max. ?target ns:humidity ?hum. }"
        res = g.query(query)
        for elmt in res:
            element =  elmt.asdict()
            for key in element:
                element[key] = element[key].toPython()
            if element['name'] == city:
                response.append(element)
        print(response)
        for i in range(len(response)):
            ToHtml += "<li><b>" + str(response[i]['name']) + "</b> — description: "  + str(response[i]['des']) + "; temperature: " + str(response[i]['temp']) +"; min: " + str(response[i]['min']) +"; max: " + str(response[i]['max']) +"; humidity: " + str(response[i]['hum']) +"</li>"
            ToJs += "L.marker([" + str(lat) + ", " + str(lon) + "]).addTo(mymap).bindPopup('City<br><b>" + str(response[i]['name']) + "</b><br>description: "  + str(response[i]['des']) + "; temperature: " + str(response[i]['temp']) +"; min: " + str(response[i]['min']) +"; max: " + str(response[i]['max']) +"; humidity: " + str(response[i]['hum']) + "');\n"
        return (ToHtml, ToJs,lat,lon)
    
# Creating API generation functions

app = Flask(__name__, template_folder='templates', static_url_path="/static", static_folder='static')

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/resultcity/', methods = ['POST'])
def predictSite():
    # Gathering input data
    latitude = 46.30
    longitude = 2.30
    # Calculating by position
    output = CityPosition()
    return render_template("resultcity.html", output_text=output[0], output_map=output[1], latitude=latitude, longitude=longitude)

@app.route('/resultweather/', methods = ['POST'])
def predictweather():
    # Gathering input data
    if request.form['city'] == '':
        city = "Paris"
    else:
        city = request.form['city']
    if request.form['type_query'] == '':
        type_request = "weather"
    else:
        type_request = request.form['type_query']
    type_text = ''
    if type_request == 'Weather':
        type_text = 'Weather'
    elif type_request == 'Air_Pollution':
        type_text = 'Air Pollution'
    elif type_request == 'both':
        type_text = 'Weather and Air Pollution'
    # Calculating by position
    output = CityWeather(city,type_request)
    return render_template("resultweather.html", output_text=output[0], output_map=output[1], latitude=output[2], longitude=output[3], type_text=type_text)

if __name__ == '__main__':
    
    app.run(debug = False, host='127.0.0.1')