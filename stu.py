#Mini project
import pandas as pd
data ={
    'name':['Alice','Bob','Charlie','David'],
    'math':[85,67,78,89],
    'Science':[92,45,84,47],
    'English':[88,92,84,90]
}

df = pd.DataFrame(data)
df['total'] = df[['math','Science','English']].sum(axis=1)
df['Avrage'] = (df['total']/3).round(2)
print(df)
# Grade based on average marks 

def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    else:
        return 'D'
df['grade'] = df['Avrage'].apply(grade)
print(df)   

# Save the Dataframe to csv file
df.to_csv("Stusent_grade.csv",index=False)