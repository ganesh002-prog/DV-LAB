##Experiment No. 3
##Basic Visualization in R

//Aim:
To create a basic line graph using R programming.


//Description:
This program creates a basic line graph using R programming. Two vectors, X and Y, are created to store the data values. 
The plot() function is used to display the graph with blue circle markers. 
The graph title and X-axis and Y-axis labels are added to make the graph easy to understand.

//Algorithm:
1.Create vectors for X and Y values.
2.Use the plot() function to draw the graph.
3.Add the graph title and axis labels.
4.Execute the program.
5.Observe the output.

//program:1 -Line Graph

x <- c(1,2,3,4,5)
y <- c(10,15,12,18,20)
plot(x, y,
     type="o",
     col="blue",
     main="Line Graph",
     xlab="X Values",
     ylab="Y Values")


2 -  Bar Chart
marks <- c(75,85,60,90,80)
barplot(marks,
        names.arg=c("Tamil","English","Maths","Science","Computer"),
        col="green",
        main="Subject Marks",
        xlab="Subjects",
        ylab="Marks")

3-Pie Chart
values <- c(30,25,20,15,10)
labels <- c("Tamil","English","Maths","Science","Computer")
pie(values,
    labels=labels,
    col=rainbow(5),
    main="Subject Distribution")

4. Scatter Plot
x <- c(2, 4, 6, 8, 10)
y <- c(5, 9, 7, 12, 15)

plot(x, y,
     col = "red",
     pch = 19,
     main = "Scatter Plot",
     xlab = "X Values",
     ylab = "Y Values")

5. Histogram

marks <- c(45, 55, 60, 65, 70, 75, 80, 85, 90, 95)

hist(marks,
     col = "orange",
     main = "Distribution of Marks",
     xlab = "Marks",
     ylab = "Frequency")


Libraries        Functions Used
- plot()         Creates line graphs and scatter plots.
- barplot()      Creates bar charts.
- pie()          Creates pie charts.
- hist()         Creates histograms.
- Base R graphicsProvides built-in visualization functions without requiring external packages.


//Result:
Thus, the line graph, bar chart, pie chart, scatter plot, and histogram were created successfully using R programming.
