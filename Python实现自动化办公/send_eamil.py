import yagmail # pip3 install yagamil

def send_email(name, to, filepath):
    contents = [
        f'{name}, 你好，你的汇报数据已整理发送到邮件附件中', 
        filepath]

    yag = yagmail.SMTP(
        user='my_email_liao@sina.com',
        password='84f462fc24029511',
        host='smtp.sina.com'
    )

    yag.send(to=to, subject='汇报数据', contents=contents)