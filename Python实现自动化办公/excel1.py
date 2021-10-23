import os
import pandas as pd
# xlrd openpyxl
from send_eamil import send_email

# excel_path = input('excel文件路径: ')

excel_path = '渠道数据分析总表.xlsx'

# 读入
data = pd.read_excel(excel_path)

names = {
    '翟丹': 'myemailliao@163.com',
    '陈文': 'myemailliao@163.com',
}
dirname = 'exceldir'

if not os.path.exists(dirname):
    # 创建文件夹路径
    os.makedirs(dirname)

for name, email in names.items():
    df = data.loc[data['负责人'] == name]
    filepath = os.path.join(dirname, f'{name}.xlsx')
    writer = pd.ExcelWriter(filepath)
    df.to_excel(writer, 'Sheet1')
    writer.save()
    if email:
        # send email
        send_email(name, email, filepath)

