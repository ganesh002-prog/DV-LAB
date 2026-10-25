//Experiment No. 7
//Creating Scatter Plot Maps in Tableau

//Aim:
To create scatter plots and map-based visualizations using Tableau.

//Description:
A scatter plot displays the relationship between two numerical variables. 
Tableau can also create map-based visualizations using geographical fields such as city, state, country, and region. 
These visualizations help analyze patterns, identify clusters, and understand regional business performance.

//Uses:
* Finding relationships between numerical variables.
* Identifying clusters and unusual values.
* Comparing sales and quantity.
* Displaying geographical information.
* Analyzing regional business performance.

//Algorithm:
1.Open Tableau Public.
2.Connect to the required dataset.
3.Identify geographical and numerical fields.
4.Drag the required numerical fields to Columns and Rows.
5.Select Scatter Plot from the Show Me panel.
6.For map visualization, use geographical fields such as City or Region.
7.Analyze the visualization and save the workbook.

//Program:
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales_map_data.csv")
plt.scatter(data["Sales"], data["Quantity"])
plt.xlabel("Sales")
plt.ylabel("Quantity")
plt.title("Scatter Plot: Sales vs Quantity")
plt.show()

//Libraries Used
1. Pandas: Used for loading and processing the dataset.
2. Matplotlib: Used for creating and displaying the scatter plot.

//sample csv file:
City,Region,Sales,Quantity
Hyderabad,South,55000,2
Delhi,North,20000,3
Mumbai,West,30000,4
Chennai,South,25000,2
Kolkata,East,15000,5
Bangalore,South,40000,3



//Result:
Thus, scatter plots and map-based visualizations were studied and created using the given sales dataset.
