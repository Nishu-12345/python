import pandas as pd

# pandas data structure
# 1. Series (1d)
# data = pd.Series([1,2,3])
# print(data)

# # Dataframe (2d)
# data = {
#     "name": ["Alice","Bob", "Joe"],
#     "marks": [67,45,23]
# }
# print(pd.DataFrame(data))

# Write a csv file

# df = pd.DataFrame(data)
# print(df)
# df.to_csv("data.csv",index=False)

# df = pd.read_csv("MOCK_DATA.csv")
# print(newData)

# print(newData.head(2)) # Display the first 2 row
# print(newData.tail(2)) # Display the last 2 row

# print(newData.shape) # Display the shape of the Dataframe
# print(newData.columns) # Display the columns of the Daraframe

# print(df['first_name']) # Display specific columns
# print(df[['first_name','email']]) # Display apecific columns

# print(df.iloc[0]) # Display the first row
# print(df.iloc[0:3]) #Display the first 3 rows

# print(df.loc[0, 'gender']) # Display thenname of the first row

# print(df[df['first_name']=='Alia']) #Display the name of the first row

# print(df[df['id'] > 7]) #Display rows where mrp is greater than 7

# print(df)

# df['grade'] = ['A','B','C'] # Add a new column

# print(df)
# df['pass'] = df['marks'] >70
# # print(df)

# df.to_csv("MOCK_DATA.csv", index=False) # Save the Dataframe to a csv file
# print(df)


# print(df)
# df.drop('pass',axis=1, inplace=True) # Dro the 'pass' column
# print(df)

# # Drop the row with index 1
# df.drop(0,axis=0, inplace=True)
# print(df)

# print(df)
# df.sort_values(by='marks',inplace=True,ascending=False)


# print(df)
# # avg_marks = df['marks'].mean()
# # max_marks = df['marks'].max() 
# min_marks = df['marks'].min() 
# sum_marks = df['marks'].sum()
# print(max_marks)
# print(min_marks)
# print(sum_marks)

# def calPass(marks):
#     return marks>70
# def half_marks(marks):
#     return marks / 2
# df ["pass"] = df['marks'].apply(calPass)
# df["half_marks"] = df['marks'].apply(half_marks)
# df["double"] = df["marks"].apply(lambda x:x*2)
# print(df)

