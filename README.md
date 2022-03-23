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
  * [About the project](#about_the_project) 
    * [Introduction](#introduction)
    * [Tasks achieved](#tasks_achieved)
    * [Conclusion](#conclusion)
  * [Usage - API](#usage)


## About the project

### Introduction

*This project is the final project of ESILV course Web Datamining And Semantics* 
<br>
For this project, we have chosen had to study a compilation of 3 different datasets from 3 API about weather, Air Quality and Location using geolocated data, in order to realise an Weather Quality application for French cities. <br> We have chosen to realise this project in Python Language, as we are more familiar with it. 

<br> 
**Main files and steps** 
<br>
The project contains a preliminary data selection [see this file](https://github.com/benptr/Web_datamining_WeatherQuality/main/apiAirQuality.py), data cleaning, data exploration and data exportation on a [Jupyter Notebook](https://github.com/benptr/Web_datamining_WeatherQuality/main/Data_creation_csv.ipynb).
<br>
The project also include our primary [ontology model](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/ontology.owl) and the [populated one](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/final_ontology.owl), both realized on Protégé. 
<br>
The project also includes the SPARQL queries we created on Protege according to our dataset listed in this [Word document](https://github.com/benptr/Web_datamining_WeatherQuality/main/SPARQL_QUERIES.docx).
<br>
Finally, the project also includes an application displaying the different criterias we want to analyse and predict, accessible by running this [file](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/app.py).

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
We created several SPARQL Queries directly on the Snap SPARQL Query window of Protégé listed in this [Word document](https://github.com/benptr/Web_datamining_WeatherQuality/main/SPARQL_QUERIES.docx). Those queries will be then used for our final application.
<br><br>
•  **Part IV - Making the application**
<br>
Here is the [Script Python](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/app.py) we used to create our final application. We decided to use the framework Flask to design our web app. <br> In this app, the user can get the location of any French city on a map and can display Weather information and Air Quality information of a specific city. We used html to try to make our app user friendly. 
<br> <br>
### Conclusion
This project has represented a real challenge for our team, both in its understanding and its realization. Indeed, we did not necessarily have all the skills required from the point of view of ontologies / creation of SPARQL queries, which required significant research work. We appreciated the freedom taken on this subject to choose our own dataset and clean our data according to the targeted features. Finally, we also enjoyed making the final functional application. <br>
In amelioration, we thought about actualising data in real time by turning our notebook into a Python script that would actualize by itself but we decided not to included this in our final version of our web app because this ncreases to much the computational demand. We prefered to have a quicker access to the results displayed rather than a two minutes or more running app every time the user enters some information.

### Usage - API 
To launch our API, you need to clone (or fork) the whole project. 
Then you need to open it on VS Code.
You have to launch the [Python Final Script](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/app.py) by typing on the Terminal Console "python app.py". <br>
![image](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/screen1.png)
<br><br> 
Then you have to click on the link that will open the app on the browser. <br>
![image](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/request.png)
<br><br>
You will arrive on this page, where you can display all the city and their precise coordinates on a map (by clicking on the first city button)
You can also search by city and select different options to display about the weather or AirPollution or both. <br> 
To make it run, you then have to follow the written instructions to display the wanted result. Here is what we can obtain by typing "Bordeaux" and selecting AirPollution Option: 
<br><br>
![image](https://github.com/benptr/Web_datamining_WeatherQuality/blob/main/results_air_pollution.PNG)
