//Experiment No. 10
//Storytelling in Tableau

//Aim:
To create a story in Tableau by arranging multiple visualizations as a sequence of insights that explain the data step by step.

//Description

Data storytelling means presenting data through an ordered series of visualizations, each supported by a short explanation.
In Tableau, a Story is made of story points.
Each story point holds one worksheet or dashboard along with a caption, so the viewer can move from one insight to the next and follow the analysis in a logical order. 
This makes the findings easier to understand, especially for people without a technical background.

//Uses:
Presenting analytical findings clearly
Explaining trends and patterns step by step
Combining charts into a logical sequence
Supporting business presentations
Communicating insights to non-technical users

//Algorithm
1.Start Tableau Public.
2.Connect to the required dataset (Excel/CSV).
3.Create the individual charts, each on its own worksheet.
4.Create a dashboard if required.
5.Click the New Story tab at the bottom.
6.Add story points by dragging worksheets or dashboards onto the story canvas.
7.Arrange the story points in a logical sequence.
8.Add a caption to each story point to explain the insight.
9.Review the story, then save or publish it.

//program:
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales_data.csv")
# STORY STEP 1: Category performance
category_sales = data.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Story 1: Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()
# STORY STEP 2: Regional contribution
region_sales = data.groupby("Region")["Sales"].sum()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Story 2: Sales by Region")
plt.ylabel("")
plt.show()
# STORY STEP 3: Quantity and sales relationship
plt.scatter(data["Quantity"], data["Sales"])
plt.title("Story 3: Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()
print("Story Created: Category performance, "
"regional distribution, and sales trends analyzed.")

//Libraries used
Pandas: loading, grouping and analyzing the data
Matplotlib: creating the bar, pie and scatter charts
Tableau: arranging the visualizations as story points and presenting the insights interactively.

//Sample Output:
Three story views are displayed:
Story 1: Bar chart of sales by category
Story 2: Pie chart of sales by region
Story 3: Scatter plot showing the relationship between quantity and sales

//Result:
Thus, storytelling was successfully implemented in Tableau to present data insights effectively.
