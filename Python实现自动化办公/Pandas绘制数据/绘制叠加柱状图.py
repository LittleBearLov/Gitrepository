import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('\Gitrepository\Python实现自动化办公\exceldir\job.xlsx')

#新计算出一个总量，用于排序
users['Total'] = users['Jan'] + users['Feb'] + users['Mar']
#排序
users.sort_values(by='Total',inplace=True)
#水平的叠加柱状图，barh中的h表示horizontal 水平的,bar是垂直的
#利用stacked就可实现叠加形式
users.plot.barh(x='Name',y=['Jan','Feb','Mar'],stacked=True)

#紧凑型布局（因为x轴文字比较长，为了让其显示全，使用紧凑型布局
plt.tight_layout()
plt.show()