import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

regex = re.compile(
    r'\$?(?:(?:[1-9][0-9]{0,2})(?:,[0-9]{3})+|[1-9][0-9]*|0)(?:[\.,][0-9][0-9]?)?(?![0-9]+)'
)

df2 = pd.read_csv('Table-25-2018-19.csv',header=14)

array = df2['Salary band'].unique()
print(array)
dict1 = {}
for item in array:
    dict1[item] = regex.findall(item)
    if not dict1[item] == []:
        dict1[item] = int(dict1[item][len(dict1[item])-1].replace(',',''))

for key in dict1.keys():
    if not dict1[key] == []:
        df2.loc[df2['Salary band'] == key,'Salary band'] = dict1[key]

print(df2)

# df = pd.read_excel('https://ncses.nsf.gov/pubs/nsf21308/assets/data-tables/tables/nsf21308-tab048.xlsx',header=4)

# df = df.rename(columns={
#     'Unnamed: 0' : 'Field',
#     'Male' : 'TotalMale',
#     'Female' : 'TotalFemale',
#     'Total' : 'EmploymentTotal',
#     'Male.1':'EmploymentMale',
#     'Female.1':'EmploymentFemale',
#     'Total.1':'PostdoctoralStudyTotal',
#     'Male.2': 'PostdoctoralStudyMale',
#     'Female.2': 'PostdoctoralStudyFemale'})

# # fig = sns.barplot(data=df,orient='h')
# # plt.show()

fig = sns.barplot(x=df2['Subject area of degree'], y=df2['Salary band'])
plt.show()