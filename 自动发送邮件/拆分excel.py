import os
import pandas as pd
# xlrd openpyxl
from send_eamil import send_email

#excel_path = input('excel文件路径: ')

excel_path = 'C:\Gitrepository\自动发送邮件\渠道数据分析总表.xlsx'
#C:\Gitrepository\自动发送邮件\渠道数据分析总表.xlsx
# 读入
data = pd.read_excel(excel_path)

names = {
    '翟丹': 'sbyu@admin.ecnu.edu.cn',
    '陈文': 'sbyu@admin.ecnu.edu.cn',
}
dirname1 = 'exceldir'

if not os.path.exists(dirname1):
    # 创建文件夹路径
    os.makedirs(dirname1)

for name, email in names.items():
    df = data.loc[data['负责人'] == name]
    filepath = os.path.join(dirname1, f'{name}.xlsx')
    writer = pd.ExcelWriter(filepath)
    df.to_excel(writer, 'Sheet1')
    writer.save()
    #如果有邮件
    if email:
        #send email
        send_email(name, email, filepath)

