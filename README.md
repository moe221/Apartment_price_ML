# Berlin Apartment Rental Price Predictor - Overview

* Implemented three different Machin learning models that could estimate the total rent price (Warmmiete) of an apartment in berlin with a MAE of  170 €.
* Used two different datasets scrapped from Immobilienscout24.de.
* The raw data consisted of rental offers posted on Immobilienscout24 in Sep 2018, May 2019, Oct 2019, Feb 2020 and Apr 2020.
* Cleaned and joined the two datasets as well as created new features from the description of each listing on ordered to identify the most important documents that are asked for when applying for an apartment. 
* Conducted an extensive EDA in order to develop insight on the rental market in Berlin.
* Used GridsearchCV to find the best hyperparameters for a Random Forest Regression.

<img align="center"src="https://github.com/moe221/Apartment_price_ML/blob/main/Images/Berlin-map.png"> 


## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, scipy, plotly, statsmodels, geopandas
**Code references and ideas:  
- Geolocation- plot code : https://juanitorduz.github.io/germany_plots/
- Preprocessing:  365 DataScience (Udemey Course)
- Model selection and tuning: Data Science Project from Scratch, Ken Jee (https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg)
** Data source 1:** https://www.kaggle.com/corrieaar/apartment-rental-offers-in-germany
** Data source 2:** https://www.kaggle.com/phanindraparashar/germany-housing-rent-and-price-data-set-apr-20


## Data Joining
The two datasets contained over 300,000 listings from all over Germany. The datasets were joined together based in their unique ScoutID and all duplicate entries were removed.
The joined dataset contained 42 columns, only the following columns were considered to be relevant to this project:
 *  regio1             
 *  serviceCharge    
 *  heatingType       
 *  newlyConst        
 *  balcony           
 *  totalRent 
 *  baseRent        
 *  hasKitchen        
 *  cellar            
 *  baseRent          
 *  livingSpace       
 *  condition         
 *  interiorQual      
 *  lift             
 *  typeOfFlat         
 *  geo_plz           
 *  noRooms           
 *  floor             
 *  numberOfFloors    
 *  garden                       
 *  regio3            
 *  description       
 *  date              
 *  yearConstructed
 


## Data Cleaning
Since the data was scrapped from a website, there were many missing values and false entries that needed to be corrected before moving on to the EDA. The following changes were made to the data:
* Only apartment offers in Berlin were considered
* Removed all duplicate listings
* Made sure that each column contained only one datatype 
* Created a column the contains the building’s age in years based on the construction year
* Parsed documents required for rental from the listings description and created a column for the most important documents (Schufa, ID, Income proof, etc.)
* Added a column for utility cost based on total rent and base rent
* Parsed neighborhood name from regio3 column
## EDA
In order to understand the data obtained from the cleaned dataset, a short analysis was conducted to develop insight and locate correlations and relationships between total rent and the other features. 

<img align="center" src="https://github.com/moe221/Apartment_price_ML/blob/main/Images/heatmap.png"> 
<img align="center" src="https://github.com/moe221/Apartment_price_ML/blob/main/Images/boxplot-noRooms.png"> 

## Model Building
Three different regression models were tested on the data, namely Multiple linear Regression, Lasso Regression and Random Forest. 
The following evaluation metrics were used to compare the performance of the models:
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R-squared (R²)
The best hyperparameters for the Random Forest model were chosen using the GridsearchCV method

## Results 
Each model’s performance is shown in the following table: 
   
| **Evaluation Metric| Multiple linear Regression| Lasso Regression| Random Forest** |
|--------------------|:-------------------------:|----------------:|----------------:|
| **MAE  [€]**       |          194.92           |     194.92      |    166.94       |
| **RMSE [€]**       |          277.76           |     277.76      |    259.80       |
| **R²   [-]**       |           0.85            |      0.85       |     0.87        |

