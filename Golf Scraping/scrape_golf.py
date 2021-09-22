import requests
from twilio.rest import Client

URL = "https://secure.east.prophetservices.com/OwlsNestV3/(S(5hysqu4le4veclvx1423ubq0))/Home/nIndex?CourseId=2&Date=2021-9-25&Time=AnyTime&Player=2&Hole=18"
content = requests.get(URL).content.decode('UTF-8')

goal_strs = ["teetime='3:2", "teetime='3:1", "teetime='3:0", "teetime='2", "teetime='1", "teetime='12", "teetime='11"]
for goal in goal_strs:
    if goal in content:
        # code adapted from https://www.twilio.com/docs/sms/quickstart/python
        account_sid = open("account_sid.txt", "r").readline()
        auth_token = open("auth_token.txt", "r").readline()
        client = Client(account_sid, auth_token)
        client.messages \
            .create(
                body="Good news! A tee time before 3:30pm has opened up for Saturday. Book it fast! https://secure.east.prophetservices.com/OwlsNestV3/Home/TeeSheet",
                from_='+12016763705',
                to='+16176108187'
            )
        break