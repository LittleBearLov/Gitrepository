import yagmail # pip3 install yagamil

def send_email(name, to, filepath):
    #邮件内容
    contents = [
        f'{name}, 你好，你的汇报数据已整理发送到邮件附件中', 
        filepath]

    yag = yagmail.SMTP(
        user='1072606373@qq.com',
        password='nmxnfwxlprjmbdfa',
        host='smtp.qq.com'
    )

    yag.send(to=to, subject='汇报数据', contents=contents)