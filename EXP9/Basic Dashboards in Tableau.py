//Experiment No. 9
//Creating Basic Dashboards in Tableau

//Aim:
To build a basic dashboard in Tableau by combining several visualizations into a single interactive view.

//Description:
A dashboard brings multiple visualizations together on one screen. 
Instead of opening charts one by one, the user can see different aspects of the data side by side, compare them, and understand overall performance at a glance.
In Tableau, each chart is first built on its own worksheet, and these worksheets are then arranged on a dashboard.
Filters and actions can be added so that selecting a value in one chart updates the others.

//Uses:
1.Combining multiple charts in one view
2.Monitoring key performance indicators (KPIs)
3.Comparing categories and regions
4.Supporting interactive analysis
5.Presenting information clearly to decision makers

//Algorithm
1.Start Tableau Public.
2.Connect to the required dataset (Excel/CSV).
3.Create the individual charts, each on its own worksheet.
4.Click the New Dashboard tab at the bottom.
5.Drag the worksheets from the left pane onto the dashboard canvas.
6.Add filters and interactive elements such as dashboard actions.
7.Arrange and resize the layout, and add titles and legends as needed.
8.Save or publish the dashboard.

//program:
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales_data.csv")
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()
data.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.show()
plt.plot(data["Quantity"], data["Sales"])
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

//Libraries used
Pandas: loading and grouping the data
Matplotlib: creating the sample charts
Tableau: combining the visualizations into an interactive dashboard

//sample output:
The program produces three analytical views:
Bar chart: sales by category
Pie chart: sales by region
Line chart: sales versus quantity

  
//Result:
Thus, a basic dashboard was successfully created in Tableau using multiple visualizations.
