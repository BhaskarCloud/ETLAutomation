import pandas as pd

# Print the Pandas version
print(pd.__version__)

source =pd.read_csv("Employee.csv",sep=",")


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


