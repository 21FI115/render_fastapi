from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# 課題9-1
@app.get("/index", response_class=HTMLResponse)
def index():
    html_content = """
    <html>
        <head>
            <title>ホームページ・メイカー</title>
        </head>
        <body>
            <h1>こんにちは！これはFastAPIで作ったHTMLページです。</h1>
            <p>FastAPIでHTMLを返すことができる。</p>
            <a href="/omikuji">おみくじを引く</a>
        </body>
    </html>
    """
    return html_content

# 課題9-2
@app.get("/omikuji")
def omikuji():
    fortunes = {
        "大吉": "大吉︕素晴らしい幸運が舞い込むでしょう。",
        "中吉": "中吉︕努力が実を結び、良い結果が待っています。",
        "小吉": "小吉︕ちょっとした幸運があなたの元にやってきます。",
        "吉": "吉︕安定した幸せな日々が続くでしょう。",
        "末吉": "末吉︕努力が実り始め、良い方向に進む時期です。",
        "凶": "凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶": "小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶": "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    }

    choice = random.choice(list(fortunes.keys()))
    return {"result": choice, "message": fortunes[choice]}
