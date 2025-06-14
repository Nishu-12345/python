import pandas as pd
# data ={
#     'Name':['Sunaina','Saniya','Kamni','Nishu'],
#     'Math':[87,89,79,67],
#     'Science':[47,68,89,47],
#     'English':[49,79,46,49]
# }
# df = pd.DataFrame(data)
# print("Math count -",(df['Math']>=80).sum())
# print("Science count -",(df['Science']>=70).sum())
# print("English count -")


 #Create a dataframe of product with price and quantity and add a column for tota cost

data = {
    'Product':['pen','Notebook','Pencil'],
    'Price':[10,25,5],
    'Quantity':[3,2,10]
    
}
df = pd.DataFrame(data)

df['total']= df['Price']*df['Quantity'] 
print(df)
# df['Avrage'] = (df['total']/3).round(2)
# df.sort_values(by='Avrage',inplace=True,ascending=False)
# print(df)
# def grade(avg):
#     if avg >= 90:
#         return 'A'
#     elif avg >= 80:
#         return 'B'
#     elif avg >= 70:
#         return 'C'
#     else:
#         return 'D'
# df['grade'] = df['Avrage'].apply(grade)
# print(df)   

# # Save the Dataframe to csv file
# df.to_csv("",index=False)


# pass= df['Science']>=80]['Name']
# # # print(df)
# # print(names)

# # df = pd.read_csv("MOCK_DATA.csv") 
# # print(df['name'])|
