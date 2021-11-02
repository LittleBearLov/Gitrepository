from twilio.rest import Client

#your account sid from twilio .com/console
account_sid = 'AC39bca2acd5d6308d8abae410ee031f76'
#your auth_token from twilio .com/console
auth_token = '3b5d61c75f64b7db76846c125c245f3b'

client = Client(account_sid,auth_token)

#通过from_将短信内容发给 to
message = client.messages.create(
    to="+8613261504183" , #已认证的手机号，+号与区号不能省略
    from_="+13186669984" ,#twilio分配的手机号，+号不能省略
    body="这是一条来着python自动化办公的短信")

print(message.sid)
