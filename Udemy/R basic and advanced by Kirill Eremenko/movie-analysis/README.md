# Movie Analysis

This is an R file aiming to analyze the correlation between the genre of the movies with the critic ratings or the audience ratings or to analyze critic ratings against the audience ratings. 
There are several plots in the code which are explained below

# Section 1- Aesthetics

a1) Here we have created a plot object with critic rating on the x axis and the audience rating on the y axis

a2) Here we have created a plot object with critic rating on the x axis and the audience rating on the y axis and we have added the geometry of point to the object which creates a scatter plot. 

a3) Here we have created a plot object with critic rating on the x axis and the audience rating on the y axis and the dots are colored according the genre of the movies. We have added the geometry of point to the object which creates a scatter plot.

a4) Here we have created a plot object with critic rating on the x axis and the audience rating on the y axis and the dots are colored according the genre of the movies and the dots are sized according to the budget of the movie in millions. We have added the geometry of point to the object which creates a scatter plot.

### Plot p

Here we have created a plot object named “p” which contains a plot with critic rating on the x axis and the audience rating on the y axis. The dots are colored according to the genre of the movie and are sized according to the budget of the movie.

In the next step we have assigned the point geometry to the plot which creates a scatter plot. 

In the next step we have assigned the line geometry to the plot which creates a line plot 

In the next step we have assigned the line geometry and the point geometry simultaneously to the plot using the layer property of R which creates a scatter plot with lines connecting the points of the similar color. 

# Section 2- Overriding Aesthetics

### Plot q
In the first step we have created a plot objects which contains a plot with critic rating on the x axis and the audience rating on the y axis. The dots are colored according to the genre of the movie and are sized according to the budget of the movie. 

In the next step we are assigning the point geometry to the plot which creates a scatter plot. 

In the first example, we are overriding the aesthetic of size to size the dots according to the critic rating of the movie instead of the budget of the movie

In the second example, we are overriding the aesthetic of color to color the dots according to the budget of the movie instead of the genre 

In the third example, we are overriding the aesthetic of x to plot the budget of the movie on the x axis instead of the critic rating and we are adding an x label of “Budget in million $). 

In the fourth example we are adding the point geometry and line geometry layer wise to create line chart and scatter plot simultaneously. 

In the example named reduce the line size, we are reducing the line size of the plot in the fourth example to 1 so that the lines become thinner and the points are clearly visible 

# Section 3- mapping vs setting 

### Plot r
We have created a plot object with critic rating on the x axis and the audience rating on the y axis and we have added the point geometry which creates a scatter plot 

Add color section

In #1 we have set the aesthetic attribute of geom_point() function to have color = genre which means that we are mapping it to a variable which in turn colors the dots corresponding to a particular movie according to the genre that movie belongs to. 

In #2 we have set the color attribute of the geom_point() function to have color = “darkgreen” which means that we are setting the color to dark green which colors all dots corresponding to a variable dark green irrespective to the genre a particular movie belongs to 

Change size section 

In #1 we are setting the aesthetic of size in the geom_point () function to BudgetMillion which means that we are mapping it to a variable which sets the size of the dots corresponding to a particular movie according to its budget. 

In #2 we are setting the size attribute of geom_point () function to 10 which means that all the dots corresponding to a movie will be sized to 10 irrespective to the budget of the movie 

In #3 we are setting the aesthetic of size in the geom_point () function to 10 which means that it will assume a random size and set it to the category of 10 and set the size of dots corresponding to a particular movie to that random size irrespective to the  budget of a movie 

# Section 4- Histograms and Density Charts

### Plot s

We have created a plot object with movies on the Budget on the x axis and then we have assigned a geometry of histogram to it with the width of each bin as 10 units. 

This creates a histogram with budget on x axis and the number of movies on the y axis. 

Add color section 

We are assigning the histogram geometry to the plot object and specifying the bin width as 10 units and setting the aesthetic of fill to genre which fills the bins of the histogram according to the genre of the movie 

Add border section 

We are assigning the histogram geometry to the plot object and specifying the bin width as 10 units and setting the aesthetic of fill to genre which fills the bins of the histogram according to the genre of the movie and setting the color to black which colors the borders of the bin as black. 

Density chart section 

In the first line we are assigning the geometry of density to the plot object and mapping the fill aesthetic to genre which creates a probability density function of the budget of movies and the number of movies which have that particular budget and fills it according to the genre of the movie 

In the first line we are assigning the geometry of density to the plot object and mapping the fill aesthetic to genre and setting the position to stack which creates a probability density function of the budget of movies and the number of movies which have that particular budget and fills it according to the genre of the movie and stacks the layers corresponding to the genre over each other so that each genre is visible clearly in the probability density function. 

# Section 5- Starting Layer tips

### Plot t 

We are creating a plot object which has audience rating on the x axis and then assigning the histogram geometry and setting the bin width to 10 which causes each bin of the histogram to be 10 units wide, then setting the fill to white which causes the bins to be filled with white color and setting the color to blue which causes the borders to be colored with blue. 

ANOTHER WAY 

First create a plot object with data = movies dataframe 

Then set the geometry to histogram and in the geom_histogram () function set the bin width to 10 and in the aesthetics set the x aesthetic to the column you want the histogram to be plotted on (in this case it is set to audience rating). Then set the fill to white and color to blue as we have done above. In this approach we can change the column as we like without modifying the plot object. 

In this way we need not rely on overriding 

# Section 6- Statistical transformations

### Plot u 

We are creating a plot object with critic rating on the x axis and audience rating on the y axis and setting the color aesthetic to genre so that each dot representing a movie gets filled with a unique color corresponding the genre to which that movie belongs to. We are applying the point geometry to create a scatter plot and applying a smooth geometry with no fill to get a smoothened plot which aids our eye and makes it easier to interpret the plot 

Section- boxplot 

We are creating a plot object with genre on the x axis and audience rating on the y axis and setting the color aesthetic to genre so that each box representing a genre gets filled with a unique color corresponding to the genre to which that box belongs to. 

Then we are assigning boxplot geometry to the plot object with size = 1.2 

Then we are assigning jitter geometry to the box plot so that the points corresponding to the movies which belong to that genre are plotted in that box. 

Then we are adding the alpha aesthetic to our boxplot along with the size aesthetic and setting the alpha aesthetic to 0.5 so that the box becomes a little transparent and the plot is much better to present 

# Section 7- Using Facets

### Plot v 

We have created a plot object with movies on the Budget on the x axis and then we have assigned a geometry of histogram to it with the width of each bin as 10 units. We have set the fill aesthetic to genre so that each bin gets filled with the genre of movies it contains and we have set the color to black so that the borders are black in color.

This creates a histogram with budget on x axis and the number of movies on the y axis. 

Section- facets 

We are adding a facet grid to our plot so that it creates a grid with each section as a separate plot in that grid and we have set the scales as free so that each plot gets scaled according to the number of movies in that particular genre. 

Section- scatter plot 

### Plot w

Here we have created a plot object which contains a plot with critic rating on the x axis and the audience rating on the y axis. The dots are colored according to the genre of the movie and the size is set to 3. 

Section – facets 

w1) In this facet plot, the graph of audience rating vs the critic rating is plotted in grids divided by columns and each column represents a particular year 

w2) In this facet plot, the graph of audience rating vs the critic rating is plotted in grids where the rows are divided by the genre and the columns are divided by the year. 

w3) In this facet plot, the graph of audience rating vs the critic rating is plotted in grids where the rows are divided by the genre and the columns are divided by the year and smooth geometry is applied to make the plot easier to interpret and aids the eye. 

w4) In this facet plot, the graph of audience rating vs the critic rating is plotted in grids where the rows are divided by the genre and the columns are divided by the year and smooth geometry is applied to make the plot easier to interpret and aids the eye. The aesthetic of size is set to the budget so that the dot representing each movie is sized according to the budget of that particular movie. 

# Section 8- Co ordinates

### Plot m 

We have created a plot object with critic rating on the x axis and the audience rating on the y axis. The size aesthetic is set to budget so that the dots are sized according to the budget of the movie and the color aesthetic is set to genre which means that the dots are colored according to the genre to which the movie belongs to 

We have assigned the geometry of that plot object to point geometry which creates a scatter plot. 

Then we have set the xlim and the ylim as 50,100 so that the x axis and the y axis will only have the markings from 50 to 100

### Plot n 

We have created a plot object which has budget on the x axis 

Then we assign the histogram geometry to that plot with bin width set to 10, and fill aesthetic mapped to genre which will color the bins according to the genre to which the movie belongs to and the color is set to black which colors the border of the bins in black 

Then we set the ylim in the coord_cartesian() function from 0 to 50 so that the scale on the y axis is calibrated from 0 to 50. 

### Improve no 1 

Here we add the the coord_cartesian() function and set the y limit from 0 to 50 so that the scale on the y axis is calibrated from 0 to 50. 

# Section 9- Themes

### Plot h

We are creating a plot object named “o” which has budget on the x axis and with the help of that object we create a histogram named h which has a bin width of 10 and the fill aesthetic is mapped to genre variable which means that the bins will be filled according to the genre of the movies. The border is set to black which means that the borders of the bins will be black in color. 

Section – label formatting 

We are adding the x label which is set to Money Axis and the y label which is set to Number of Movies. The color of the x label is set to dark green and the font size is set to 30. The color of the y label is set to red and the font size is set to 30.

Section – tick mark formatting 

The font size of the text on the tick marks on both the axis is set to 20

Section – legend formatting 

The font size of the title of the legend is set to 30

The font size of the text in the legend is set to 20. 

The position of the legend is set to top right 

Section – title formatting 

The color of the text in the title is set to dark blue and the font size of the text in the title is set to 30. And the title of the plot is set to movie budget distribution in the ggtitle() function. 

# Section 10- Homework section

At first we are creating a dataframe named as hwmovies which has the data of Section6HomeworkData.csv 

Then we set the column names of the data in the hwmovies dataframe to the column names specified in the code. 

Then we create the filters which fulfill the criteria given in the question.

Then we create a new dataframe hwmovies2 which has the filters applied on the hwmovies dataframe. 

Then we create the plot object which has genre on the x axis and gross percentage in US on the y axis. 

Then we apply the jitter geometry with the size aesthetic set to budget which will size the dots representing a particular movie according to its budget. We set the color aesthetic to studio which colors the dots according to the studio which produced the movie. Then we apply the boxplot geometry with the alpha property set to 0.7 so that it becomes a little transparent and we set the outlier color to NA to get the desired result. 

### The datasets used in this project are specified in the csv files and the description of what is done in the code is given in the pdf file which is attached 
