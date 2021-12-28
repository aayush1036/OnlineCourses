# Weather Analysis 

## Intro

First we are setting the working directory to the folder in which our datasets are stored. 

Then we are importing the respective files as dataframes in the respective variables named accordingly 

#### NOTE : We have used row.names=1 so that it takes the row names from the first column and the values in the first column become row names

## Convert DataFrame to Matrix

We are converting all the variables created above to a dataframe by using the as.matrix() function 

## Lets put these into a list

We are adding the matrices created above in a list named as "Weather" by using the list() function and passing the column names as argumments in the list() function

## Lets try it out

In this section we are validating that "Weather" is a list and we are validating that by subsetting some items 

## Analyze one city

We are using the apply function to apply the mean function to all the rows in the "Chicago" matrix. In this function we have passed "Chicago" as the matrix to which the function is to be applied, we have passed 1 as the margin which specifies that the function being passed ahead is to be applied to the rows, then we are passing the function which we wish to apply to the row which is the mean function in this case. 

#### Compare
In this section we are applying the apply function with the same arguments as above to every city under our observation 

## Using lapply

In this section we are using the lapply() function and passing weather as the list to which the function specified ahead is to be applied and we are passing the transpose function as the function to be applied to each item in the list. This line of code transposes all the matrices which are present in the list. 

#### Example 2

In this example, we are using the lapply() function and passing weather as the list to which the function specified ahead is to be applied and we are passing the rbind() function and we are creating a new row named as NewRow which has the numbers 1 to 12 in it and this row will get added to each element of the list. 

#### Example 3

In this example, we are using the lapply() function and passing weather as the list to which the function specified ahead is to be applied and we are passing the rowMeans() function which calculates the mean of each row of each element of the list. 

## Combining lapply with []

In this section we are passing "[" as a function which subsets a specific row whose row number is specified ahead from each element in the list.

For example lapply(Weather, "[",1,1) extracts the element in the first row and the first column from every element in the list 

For example lapply(Weather, "[",1,) extracts the first row of every element in the list. 

For example lapply(Weather, "[",,3) extracts the third column of every element in the list. 

## Adding our own functions

We can pass custom functions that we have created in each function which comes under the apply() class

For example in lapply(Weather, function(x) x[1,]) we are extracting the first row of each element in the list by creating our own function and passing the list element as a parameter. 

## Using sapply()

sapply() function is a function which applies the function to each element in the list and returns the final product after applying the function in the form of a matrix.

For example sapply(Weather, "[", 1,7) returns the matrix for each city which contains the element stored in the 1st row and 7th column in each element of the list.

round(sapply(Weather, rowMeans),2) returns the matrix containing the mean of each row in each element of the list rounded up to 2 deciaml places. 

sapply(Weather, function(z) round((z[1,]-z[2,])/z[2,], 2)) returns the matrix fluctuation using the minimum as the base and rounded up to 2 deciaml places of each list element. The fluctuation is calculated by passing our own function which calculates the difference between the maximum and minimum temparatures and divides it by the minumum. 

## Nesting apply functions

In sapply(Weather, apply,1, max) we have nested the max function to the apply function in the sapply() function. This line of code calculates the maximum of each row of each list elenments and rerurns the output in the form of a matrix. 

## Very advanced tutorial 

We are using the which.max() function which determines the row or column name in which the maximum is located. 

For example in which.max(Chicago[1,]), the which.max() function determines the column name in which the maximum of the first row is located. 

We are using sapply(Weather, function(y) apply(y, 1, function(x) names(which.max(x)))) to create the matrix which has the names of the columns in which the maximum is located for each row of each list element 

We are using sapply(Weather, function(y) apply(y, 1, function(x) names(which.min(x)))) to create the matrix which has the names of the columns in which the minimum is located for each row of each list element 

## The datasets used in this project are specified in the csv files in the Weather Data folder and the description of what is done in the code is given in the pdf file which is attached
