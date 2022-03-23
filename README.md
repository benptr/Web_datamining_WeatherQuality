<h1 align="center">
  <br>
   <img src=https://aqicn.org/images/aqicn.png>
  <br>
  Web Datamining and Semantics Project - Weather / Air Quality App 
  <h2 align="center">
    CHMIEL Audrey & DONIER Marie & PORTERIE Benjamin
    <br>
    ESILV | DIA 1
  </h2>
</h1> 

## Table of contents
  * [About the project](#about_the_project) <br>
    * [Introduction](#introduction)
    * [Tasks achieved](#tasks_achieved)
    * [Conclusion](#conclusion)
  * [Usage - API](#usage)
  * [Architecture](#architecture)


## About the project

### Introduction

*This project is the final project of ESILV course Web Datamining And Semantics* 
<br>
For this project, we have chosen had to study a compilation of 3 different datasets from 3 API about weather, Air Quality and Location using geolocated data, in order to realise an Weather Quality application for French cities. <br> We have chosen to realise this project in Python Language, as we are more familiar with it. 

<br> 
The project contains a preliminary data selection, data cleaning, data exploration and data exportation 

The project also includes the SPARQL queries we invented on Protege according to our dataset.

Finally, the project also includes an application displaying the different criterias we want to analyse and predict.  

### Tasks achieved 

The project is organized in 3 main parts: 
<br><br>
•	 **Part I - Data selection, Data cleaning and data exportation**
<br> After some researches about our project, we decided to choose datasets from these 3 APIs: <br> 
[AirQualityApi](https://aqicn.org/api/fr/) <br>
[WeatherAPI](https://openweathermap.org/api) <br>
[Cities](https://datahub.io/core/world-cities) <br>
We then created a [Script Python](https://github.com/benptr/Web_datamining_WeatherQuality/main/apiAirQuality.py) to select the features that interested us (Citie's name, coordinates, temperature and weather condition, air quality indexes). We exported the data in a JSON file (dataFrance.json)
<br>
We then open this file in a [Jupyter Notebook](https://github.com/benptr/Web_datamining_WeatherQuality/main/Data_creation_csv.ipynb), studied the different datatypes of features, cleaned it to make it user friendly and finally exported it into 3 different CSV files (weather.csv, city.csv, airquf.csv). 
<br><br>
•	 **Part II - Modeling the Ontology, Populate the ontology**
<br>
First, we had to model our ontology using the application Protégé. We created 3 classes (Airquf, Weather and City), 11 data properties and 3 object properties, according to the features of the csv files we obtained. We defined for each properties their domain and range (according to the datatypes)
<br> Then we populated the ontology with some instances we created by hand in order to test the consistency of our ontology thanks to the reasoner. 
<br>
Finally, we had to load all the data from our csv file to our ontology. We reopened our Jupyter Notebook, imported the library RDFLIB and its different components to populate our ontology with our data matching our classes and properties defined in Protégé. Then we exported a final file in .owl format, containing our ontology populated with real data. Here is a screenshot of the ontology we obtained on Protégé: 
![image](https://user-images.githubusercontent.com/61688477/159586390-7cfed3c3-1912-465a-973a-446b5a6d85f6.png) 
<br><br>
• **Part III - Querying the ontology**
<br> 
We created several SPARQL Queries directly on the Snap SPARQL Query window of Protégé listed [Word document](https://github.com/benptr/Web_datamining_WeatherQuality/main/SPARQL_QUERIES.docx). Those queries will be then used for our final application.
<br><br>
•  **Part IV - Making the application**
 
### Conclusion

