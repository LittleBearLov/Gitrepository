import pandas as pd

students = pd.read_excel('1.xlsx', sheet_name='Sheet1')
# sort_values 按值排序，by针对某一行，ascending为False表示从大到小
students.sort_values(by='Score', ascending=False, inplace=True)
print(students)