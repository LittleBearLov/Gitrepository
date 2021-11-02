#自动接收回复的邮件
import poplib
from email.parser import Parser # 解析器
from email.header import decode_header

def connect_eamil():
    user='1072606373@qq.com',
    password='nmxnfwxlprjmbdfa',
    host='pop.qq.com'
    #开始连接到服务器
    server = poplib.POP3(host)
    #打开或者关闭调试信息
    server.set_debuglevel(1)
    #打印POP3服务器的欢迎文文字
    print(server.getwelcome().decode('utf-8'))
    #开始进行身份认证
    server.user(user)
    server.pass_(password)
    print('server connect success')
    return server

def get_email_content(server):
    #返回邮箱中的最新电子邮件
    #返回当前电子邮件总数目和占用服务器的空间大小
    email_num, eamil_size = server.stat()
    # print(f'Email Num: {email_num}')
    #根据索引ID获取电子邮件信息
    rsp, msglines, msgsiz = server.retr(email_num)
    # print(msglines)
    #接拼电子邮件内容并对内容进行GBK解码（新浪邮箱），QQ邮箱应该是utf-8
    msg_content = b'\r\n'.join(msglines).decode('utf-8')
    # 把邮件内容解析为messsage对象
    msg = Parser().parsestr(msg_content)
    #关闭与服务器的连接，释放资源
    server.close()
    return msg

def parser_subject(msg):
    #解析邮件主题
    subject = msg['Subject']
    #解析邮件
    value, charset = decode_header(subject)[0]
    #如果指定了字符集
    if charset:
        #使用改字符集进行解码
        value = value.decode(charset)
        #打印邮件主题：
        #print('邮件主题：{0}'.format(value))
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if not charset:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def parser_content(msg, indent=0):
    #有多个部门，对每个部分都进行解析
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print(f"{' ' * indent * 4} 第{n + 1}部分")
            print(f"{' ' *indent * 4} {'-' * 50}")
            parser_content(part, indent+1) #递归解析
    else:
        content_type = msg.get_content_type() #获取content_type
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg) #猜测字符集
            if charset:
                content = content.decode(charset)
                print(f"{' ' * indent * 4} 邮件内容：{content}")
        else:
            print(f"{' ' * indent * 4} 附件内容{content_type}")


def main():
    server = connect_eamil()
    msg = get_email_content(server)
    subject = parser_subject(msg)
    print(subject)
    parser_content(msg)


main()