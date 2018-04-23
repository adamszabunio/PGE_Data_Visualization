# PGE_Data_Visualization

Python and Tableau Data Visualizations
------------------------------------------------

Data science isn't just *Deep Learning* and *AI*. It is a combination of numerous skills and attributes.  One of the most important, and my favorite, is *Data Visualization* and *Communicating* the findings. 

In this repository, I sought out to:
+ Learn and practice Tableau for Data Visualization
+ Compare/Contrast Tableau and Python 
+ Find a happy medium between the two
_____________

## The Data

Data used for this project was publicly available energy consumption data for Gas and Electric utilities from [Pacific Gas and Electric](https://pge-energydatarequest.com/public_datasets).
+ Two energy utilities, Gas and Electric
+ 5 years of Monthly Consumption Quarterly data from 2013 - 2017
+ Usage data is aggregated monthly by customer class (Residential, Commercial, Industrial, or Agricultural)
+ Grouped by ZIP Code [1](EDRP Quarterly Report Notes.pdf)


## The Analysis

Samples of Data from both Utilities.  

+ Electric:
![](final_data/elec_samp.png?raw=true) 

Electric Data contains 4 unique Customer Classes.

+ Gas:
![](final_data/gas_samp.png?raw=true)

Gas Data only contains 3 unique Customer Classes.

Image below and further analysis can be found in the [Exploratory Data Analysis Jupyter Notebook](Exploratory_Data_Analysis_PGE)

![](final_data/venn.png?raw=true) 
![](final_data/unique.png?raw=true)


## Tableau VS Python 

![](final_data/comparison.jpeg?raw=true)


## Workflow using Python *then* Tableau

+ Using Pandas and Python, data was normailized and aggregated using a [Python script](unzip_and_clean.py).  
+ After [dropping the final duplicates](Exploratory_Data_Analysis_PGE.ipynb#Drop-Duplicates), data was loaded into Tableau Public.
+ Finally, [Analysis, Visualizations and Presentation were created in Tableau](https://public.tableau.com/profile/adam.szabunio#!/vizhome/PGE_Data_Visualization/PGEPresentation?publish=yes).
______