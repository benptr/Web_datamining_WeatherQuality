from rdflib import Graph, Literal, RDF, URIRef, Namespace, XSD

from rdflib.namespace import FOAF , RDF
import pandas as pd

df_weather = pd.read_csv('weather.csv',index=False)
airquf= pd.read_csv('airquf.csv',index=False)
citydata= pd.read_csv('city.csv',index=False)

# Create a Graph
g = Graph()
#g.namespace_manager.bind('rdf', Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#'))
#g.namespace_manager.bind('rdfs', Namespace('http://www.w3.org/2000/01/rdf-schema#'))
#g.namespace_manager.bind('owl', Namespace('http://www.w3.org/2002/07/owl#'))
#g.namespace_manager.bind('xml', Namespace('http://www.w3.org/1998/namespace'))
#g.namespace_manager.bind('city', Namespace('http://www.owl-ontologies.com/unnamed.owl#'))
#g.namespace_manager.bind('NS', Namespace('http://www.semanticweb.org/admin/ontologies/2022/1/untitled-ontology-30#'))
#g.namespace_manager.bind('xsd', Namespace("http://www.w3.org/2001/XMLSchema#"))
g.parse("ontology.owl")

# Create a Namespace :

NS = Namespace("http://www.semanticweb.org/admin/ontologies/2022/2/untitled-ontology-30#")

#Populate city 
for i in range(len(citydata)):
    class_city = URIRef(f"http://www.semanticweb.org/admin/ontologies/2022/2/untitled-ontology-30#City_{i}")
    g.add((class_city, RDF.type, NS.City))
    g.add((class_city, NS.city, Literal((citydata['city'].iloc[i]),datatype=XSD.string)))
    g.add((class_city, NS.latitude, Literal(float(citydata['lat'].iloc[i]), datatype=XSD.float)))
    g.add((class_city, NS.longitude, Literal(float(citydata['lon'].iloc[i]),datatype=XSD.float)))
 
# Populate weather
for i in range(len(df_weather)):
    class_weather = URIRef(f"http://www.semanticweb.org/admin/ontologies/2022/2/untitled-ontology-30#Weather_{i}")
    g.add((class_weather, RDF.type, NS.Weather))
    g.add((class_weather, NS.city, Literal((df_weather['city'].iloc[i]),datatype=XSD.string)))
    g.add((class_weather, NS.description, Literal((df_weather['description'].iloc[i]),datatype=XSD.string)))
    g.add((class_weather, NS.humidity, Literal(float(df_weather['humidity'].iloc[i]),datatype=XSD.float)))
    g.add((class_weather, NS.temp, Literal(float(df_weather['temp'].iloc[i]),datatype=XSD.float)))
    g.add((class_weather, NS.temp_max, Literal(float(df_weather['temp_max'].iloc[i]),datatype=XSD.float)))
    g.add((class_weather, NS.temp_min, Literal(float(df_weather['temp_min'].iloc[i]),datatype=XSD.float)))

#Populate airQuality
for i in range(len(airquf)):
    class_air = URIRef(f"http://www.semanticweb.org/admin/ontologies/2022/2/untitled-ontology-30#Airquf_{i}")
    g.add((class_air, RDF.type, NS.Airquf))
    g.add((class_air, NS.city, Literal((airquf['city'].iloc[i]),datatype=XSD.string)))
    g.add((class_air, NS.aqi, Literal(float(airquf['aqi'].iloc[i]),datatype=XSD.float)))
    g.add((class_air, NS.today_o3_average, Literal(float(airquf['today_o3_average'].iloc[i]),datatype=XSD.float)))
    g.add((class_air, NS.tomorrow_o3_average, Literal(float(airquf['tomorrow_o3_average'].iloc[i]),datatype=XSD.float)))

print(g.serialize(destination='final_ontology.owl', format='pretty-xml'))