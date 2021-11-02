import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

path = '\Gitrepository\Python实现自动化办公\exceldir\people.xlsx'
students = pd.read_excel(path,sheet_name='Sheet1')
students.sort_values(by='Score', ascending=False, inplace=True)

plt.bar(students.Name,students.Score,color='orange')
#设置标题、X轴名称与Y轴名称，fontsize 设置字号
plt.title('Student Score',fontsize=16)
plt.xlabel('Name')
plt.ylabel('Score')
#标题指定为中文
#添加中文字体支持
#simSun.ttc 简体字
font = FontProperties(fname=r"C:\Windows\Fonts\simSun.ttc")
plt.title('学生分数',fontProperties=font)
plt.xlabel('名字',fontProperties=font,fontsize=14)
plt.ylabel('分数',fontProperties=font,fontsize=14)
#因为X轴字体太长，利用rotation将其旋转90度，方便显示
plt.xticks(students.Name,rotation='90')

#紧凑型布局（因为x轴文字比较长，为了让其显示全，使用紧凑型布局
plt.tight_layout()
plt.show()
