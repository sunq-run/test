import os
from bottle import route, run, request
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('w3rUJmXUD8biLnl2wS3XGYEyV5i2UsDqU0bxxuQdN3cmzQWJYkaD2cML2iH63Z3qIth1BconGPaZhGQHsCr8eJeKlRZuXDP6zGEWdgFhXdDxtrW5OujEG0pwf28muDSPAEv4D+oCRlQD6uh7mDVjdgdB04t89/1O/w1cDnyilFU=')

userID = 'U969890d77500165c6c75db79486e57fa'
@route("/")
def hello_world():
        try:
            line_bot_api.push_message(userID, TextSendMessage(text='Hello World!'))
        except LineBotApiError as e:
                return "Sorry..."
        return "HELLO TAKEYUKI"
    
@route("/webhook", method='POST')
def get_info():
        data = request.json["events"]["timestamp"]
        try:
            line_bot_api.push_message(userID, TextSendMessage(text=str(data)))
        except LineBotApiError as e:
                return "asdasd"
        
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

