import pandas as pd

# Print the Pandas version
print(pd.__version__)

source =pd.read_csv("Employee.csv",sep=",")

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
print("TEST COMPLETED____\n")

print("Test Case 12: Sample ( bottom 5 ) records from source file \n")
print(source.tail())
print("\n")
print("TEST COMPLETED____\n")
