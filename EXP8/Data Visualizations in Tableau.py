#Experiment No. 8
#Data Visualizations in Tableau (Charts, Graphs and Data Mapping)

//Aim:
To design and build different charts, graphs and maps in Tableau, and to show how each one helps present data clearly.

//Description:
Each chart type suits a different analytical purpose.
Bar charts compare values across categories, pie charts show how a whole is divided into parts, line charts show how values change or trend, and maps display data by geographic location. 
Tableau lets you build all of these by dragging and dropping fields, with no coding required.
The same charts can also be produced in Python using Pandas and Matplotlib, as in the program below.

//Uses:
* Comparing different categories (bar chart)
* Showing percentage share of each part (pie chart)
* Tracking trends and changes (line chart)
* Plotting location-based data (map)
* Presenting business insights in a clear, visual form

//Algorithm
1.Start Tableau Public.
2.Connect to the required dataset (Excel/CSV).
3.Drag the needed dimensions and measures onto the Rows and Columns shelves.
4.Choose a suitable chart type from the Show Me panel.
5.Format the chart with colors, labels, titles and tooltips.
6.Review the results, then save or publish the visualization.

//program:
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales_data.csv")
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()
data.groupby("Category")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%")
plt.title("Category Distribution")
plt.ylabel("")
plt.show()
plt.plot(data["Quantity"], data["Sales"])
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

//Libraries used
* Pandas: loading and grouping the data
* Matplotlib: creating and customizing the charts

//sample output:
Three visualizations are produced:
Bar chart (Sales by Category): Electronics has the highest total sales (about 75,000+), well above Furniture (about 37,000).
Pie chart (Category Distribution): Electronics accounts for about 67.8% of sales and Furniture for about 32.2%.
Line chart (Sales vs Quantity): Sales are plotted against quantity, from 1 to 5 units.

//Result:
Thus, various charts, graphs and maps were successfully created using Tableau, and the same charts were reproduced using Python.
