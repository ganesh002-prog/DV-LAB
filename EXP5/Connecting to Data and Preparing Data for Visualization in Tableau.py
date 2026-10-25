##Experiment No. 5
#Connecting to Data and Preparing Data for Visualization in Tableau

//Aim:
To link Tableau with a data source and get the data ready for building visualizations.
                                                       
//Description:
This program prepares a sales dataset for Tableau using Python's pandas library. 
It loads the CSV file, previews the first five records and counts missing values in each column.
It then removes duplicate rows, converts the Sales column to a numeric type and saves the cleaned data to a new CSV file. 
That file can then be imported into Tableau for visualization.

//Algorithm:
1.Launch Tableau Public.
2.Choose the data source you need.
3.Load the dataset into Tableau.
4.Check that the data loaded correctly.
5.Do basic cleaning (handle missing values, remove duplicates, fix data types).
6.Save the workbook.

//program:
import pandas as pd
df = pd.read_csv("SalesData.csv")
print(df.head())
print(df.isnull().sum())
df = df.drop_duplicates()
df["Sales"] = pd.to_numeric(df["Sales"])
df.to_csv("cleaned_sales_data.csv", index=False)
print("Dataset cleaned and ready for Tableau.")


//Sample CSV File (SalesData.csv):
OrderID,Product,Category,Sales,Quantity,Region
101,Laptop,Electronics,55000,2,South
102,Mobile,Electronics,20000,3,North
103,Chair,Furniture,5000,5,West
104,Table,Furniture,7000,2,East
105,Headphones,Electronics,3000,4,South
106,Sofa,Furniture,25000,1,North

//sample output:
     OrderID     Product     Category  Sales  Quantity Region
0      101      Laptop  Electronics  55000         2  South
1      102      Mobile  Electronics  20000         3  North
2      103       Chair    Furniture   5000         5   West
3      104       Table    Furniture   7000         2   East
4      105  Headphones  Electronics   3000         4  South
OrderID     0
Product     0
Category    0
Sales       0
Quantity    0
Region      0
dtype: int64
Dataset cleaned and ready for Tableau.

//Result:
The dataset was successfully connected to Tableau, cleaned using Python (checked for missing values, removed duplicates and converted Sales to a numeric type), and saved as cleaned_sales_data.csv.
The data is now prepared and ready for creating visualizations in Tableau.
