import poplib
from email.parser import Parser # 解析器
from email.header import decode_header

def connect_eamil():
    user='my_email_liao@sina.com'
    password='84f462fc24029511'
    host='pop.sina.com'
    server = poplib.POP3(host)
    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8'))
    server.user(user)
    server.pass_(password)
    print('server connect success')
    return server

def get_email_content(server):
    email_num, eamil_size = server.stat()
    # print(f'Email Num: {email_num}')
    rsp, msglines, msgsiz = server.retr(email_num)
    # print(msglines)
    msg_content = b'\r\n'.join(msglines).decode('gbk')
    # 邮件内容
    msg = Parser().parsestr(msg_content)
    server.close()
    return msg

def parser_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
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
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print(f"{' ' * indent * 4} 第{n + 1}部分")
            print(f"{' ' *indent * 4} {'-' * 50}")
            parser_content(part, indent+1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
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