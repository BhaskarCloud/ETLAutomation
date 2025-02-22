import pandas as pd

# Print the Pandas version
print(pd.__version__)

source =pd.read_csv("Employee.csv",sep=",")

print("Test Case 0: return the all information of your dataset : \n") 
print(source.info) 
print("\n")

print("Test Case 1: Following are the column names in the source file : \n") 
print(source.columns) 
print("\n")

print("Test Case 2: Rows X colums in the source file \n")
print(source.shape)
print("\n")

print("Test Case 3: No. of rows under each columns \n")
print(source.count())
print("\n")

print("Test Case 4: Duplicate records in the source \n")
print(source.duplicated().sum())
print("\n")

print("Test Case 5: Duplicate records saved in the file below \n") 
dupes = source[source.duplicated()].to_csv("duplicated.csv") 
print("\n")

print("Test Case 6: Check if NULL value exist in dept_name column \n") 
print(source[source['dept_name'].isnull()]) 
print("\n") 

print("Test Case 7: Unique value of emp_no column in the source \n") 
print(source['emp_no'].unique()) 
print("\n")

print("Test Case 8: Unique value of emp_name column in the source \n") 
print (source [ 'emp_name' ].unique()) 
print("\n")

print("Test Case 9: Unique value of dept_name column in the source \n") 
print (source [ 'dept_name' ].unique()) 
print("\n")

print("Test Case 10: Unique value of Salary column in the source \n")
print(source['Salary'].unique())
print("\n")

print ("Test Case 11: Sample ( top 5 ) records from source file \n")
print(source.head())
print("\n")

print("Test Case 12: Sample ( bottom 5 ) records from source file \n")
print(source.tail())
print("\n")

# Randomly select n rows
print(source.sample(3))

# Select top 2 Highest Salary
print(source.nlargest(2, 'Salary'))

# Select the Salary > 2000
print(source[source.Salary > 2000])

# Select the FRUITS name
print(source['emp_name'])

# Select the FRUITS name and
# their corresponding PRICE
print(source[['emp_name', 'Salary']])


# Sorting in Ascending order
print("Test Case 13: Sorting emp_name in Ascending order \n")
print(source.sort_values('emp_name', ascending=True))
print("\n")

# Sorting in Descending order
print("Test Case 14: Sorting emp_name in Descending order \n")
print(source.sort_values('emp_name', ascending=False))
print("\n")

# Sorting by Index
print("Test Case 15: Sorting by Index in Descending order \n")
print(source.sort_index(ascending=False))
print("\n")

# Sorting by Index
# Reset the indexes to default
# inplace = True will make changes to the orginal dataframe
# drop =True will drop the initial indexes
print("Test Case 16: Reset the indexes to default \n")
source.reset_index(drop=True, inplace=True)
print(source)
print("\n")
print("TEST COMPLETED____\n")

# Renaming
df = pd.read_csv("fruits.csv",sep=",")
print(df)
df.rename(columns={'Fruits': 'FRUITS',
                   'Quantity': 'QUANTITY',
                   'Price': 'PRICE'},
          inplace=True)
print(df)

# Gather columns into rows.
print(pd.melt(df))

# Pivot table
pivot = df.pivot(columns='FRUITS',values=['PRICE', 'QUANTITY'])
print(pivot)


# Drop the DISCOUNT Columns
df1 = df.drop(columns=['QUANTITY'], axis=1)
print(df1)


# Drop 2nd and 4th rows
df2 = df.drop([1, 3], axis=0)
print(df2)


# Subsets of rows or columns
# Select all the columns between Fruits and Price
print(df.loc[:, 'FRUITS':'PRICE'])

# Select FRUITS name having PRICE <70
print(df.loc[df['PRICE'] < 70,
             ['FRUITS', 'PRICE']])

# Select 2:5 rows
print(df.iloc[2:5])

# Select the columns having ) 0th & 2nd positions
print(df.iloc[:, [0, 2]])

# Select Single PRICE value at 2nd Postion
df.at[1, 'PRICE']

# Select the single values by their position
df.iat[1, 2]

# Filter by column name
print(df.filter(items=['FRUITS', 'PRICE']))

# Filter by row index
print(df.filter(items=[3], axis=0))

# Where
df['PRICE'].where(df['PRICE'] > 50)


# QUERY
print(df.query('PRICE>70'))

# Price >50 & QUANTITY <30
print(df.query('PRICE>50 and QUANTITY<30'))


# FRUITS name start with 'M'
#print(df.query('FRUITS.str.startswith("Ma")'))
#print(df.query("FRUITS.str.startswith('M')"))

#Combine Two data sets
#Create 1st dataframe



df1 = pd.read_csv("fruit1.csv",sep=",")
print(df1)

#Create second dataframe
df2 = pd.read_csv("fruit2.csv",sep=",")
print(df2)

# Merge two dataframe
# Left Join
print(pd.merge(df1, df2,
               how='left', on='Fruits'))

# Right Join
print(pd.merge(df1, df2,
               how='right', on='Fruits'))

# Inner Join
print(pd.merge(df1, df2,
               how='inner', on='Fruits'))

# Outer Join
print(pd.merge(df1, df2,
               how='outer', on='Fruits'))

#Concatenation
# Row-wise Concatenation having the same column name



data = {'FRUITS': ['Grapes', 'Pineapple'],
        'QUANTITY': [23, 17],
        'PRICE': [60, 30]
        }

# Create Pandas Dataframe with dictionary
df1 = pd.DataFrame(data)

# Concatenate df and df1
df2 = pd.concat([df, df1], axis=0,
                ignore_index=True)
print(df2)

# Column-wise Concatenation having the same column name
data = {'DISCOUNT': [5, 7, 10, 8, 6]}

# Create Pandas Dataframe with dictionary
discount = pd.DataFrame(data)

# Concatenate df2 and discount
df = pd.concat([df2, discount], axis=1)
print(df)

#Descriptive Analysis Pandas
#Describe dataset
# For numerical datatype
print(df.describe())

# For object datatype
print(df.describe(include=['O']))

# Check the unique values in the dataset
df.FRUITS.unique()  


# Count the total unique values
df.FRUITS.value_counts()   

#Sum values
print(df['PRICE'].sum())

#Cumulative Sum
print(df['PRICE'].cumsum())


# Minimumn PRICE
df['PRICE'].min()

# Maximum PRICE
df['PRICE'].max()

# Mean PRICE
df['PRICE'].mean()

# Median PRICE
df['PRICE'].median()

# Variance
df['PRICE'].var()

# Stardard Deviation
df['PRICE'].std()

# Quantile
df['PRICE'].quantile([0, 0.25, 0.75, 1])


# Apply any custom function
def summation(col):
    if col.dtypes != 'int64':
        return col.count()
    else:
        return col.sum()


df.apply(summation)

# Covariance
print(df.cov(numeric_only=True))
#print(df.cov())


# Correlation
print(df.corr(numeric_only=True))
#print(df.corr())

# Missing Values
# Check for null values using isnull() function.
# Check for null values
print(df.isnull())

# Column-wise null values count
# Total count of null values
print(df.isnull().sum())

#Fill the null values with mean()
Mean = df.DISCOUNT.mean()

# Fill the null values
df['DISCOUNT'] = df['DISCOUNT'].fillna(Mean)
print(df)

# We can also drop null values rows using the below command

# Drop the null values
df.dropna(inplace=True)

# Add a column to the Existing dataset

# Values to add
Origin = pd.Series(data=['BH', 'J&K','BH', 'MP','WB', 'WB'])

# Add a column in dataset
df['Origin'] = Origin
print(df)
# Add a column using the existing columns values
df = df.assign(Paid_Price=lambda df:
               (df.QUANTITY * df.PRICE)\
               -(df.QUANTITY * df.PRICE)\
               *df.DISCOUNT/100)
print(df)

#Group By
#Group the DataFrame by the ‘Origin’ column using groupby() methods

# Group the DataFrame by 'Origin' column
grouped = df.groupby(by='Origin')

# Compute the sum as per Origin State
# All the above function can be
# applied here like median, std etc
print(grouped.agg(['sum', 'mean']))

#Outlier Detection using Box plot
#we can use a boxplot for Detection of the outliers.




# Box plot
df.boxplot(column='PRICE', grid=False)

# Bar Plot with Pandas
# plot.bar() method is used to plot bar in pandas.

df.plot.bar(x='FRUITS', y=['QUANTITY', 'PRICE', 'DISCOUNT'])

#Bar Plot with Pandas


# Histogram with pandas
# plot.hist() methods is used to create a histogram.
df['QUANTITY'].plot.hist(bins=3)

#Histogram with pandas

#Scatter Plot with Pandas
#scatter() methods used to create a scatter plot in pandas.
df.plot.scatter(x='PRICE', y='DISCOUNT')

#Scatter Plot with Pandas
#Pie Chart with Pandas
#plot.pie() methods used to create pie chart.
grouped = df.groupby(['Origin'])
grouped.sum().plot.pie(y='Paid_Price', subplots=True)

"""
Code snippet:



source.head(): Returns the first few rows of a DataFrame.
source.tail(): Returns the last few rows of a DataFrame.
source.info(): Provides information about the DataFrame, such as the number of rows and columns, the data types of the columns, and the missing values.
source.describe(): Provides summary statistics for the numerical columns in a DataFrame.
source.loc[row_index, column_name]: Returns the value at a specific row and column in a DataFrame.
source.iloc[row_index, column_index]: Returns the value at a specific row and column index in a DataFrame.
source.sort_values(by=’column_name’): Sorts the DataFrame by the values in a specific column.
source.groupby(‘column_name’): Groups the DataFrame by the values in a specific column.
               

               """