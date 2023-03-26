
from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import ut_line_bot

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def sendmessage(user_id,m):
    mm = TextSendMessage(text=m)
    line_bot_api.push_message(user_id,messages=mm)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "はい":
        try :
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="健康管理フォームを提出します。"))
            ut_line_bot.main()
            sendmessage("U54bf4ed3ec4c085e6c9bf0e8a9acc0d8","健康管理フォームの提出が完了しました。")
        except:
            sendmessage("U54bf4ed3ec4c085e6c9bf0e8a9acc0d8","予期せぬエラーが発生しました。手動で入力してください。")

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)