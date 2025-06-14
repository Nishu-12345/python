# import pandas as pd

# #Sample data
# data = {
#     'Name':['John','Anna','peter','lina'],
#     'Age':[28,21,20,19],
#     'City':['New York','Paris','London','Sydeny']
# }

# # Create pandas dataframe
# df = pd.DataFrame(data)


# # define file path
# file_path = 'xlsx'

# # Write dataframe to excel
# df.to_excel(file_path,index=False)

# print("Excel file has been created successfuly!")


import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Accessing a column
print("\nNames only:")
print(df['Name'])

# Filter rows where Age > 28
print("\nPeople older than 28:")
print(df[df['Age'] > 28])
