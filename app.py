import socket

from flask import Flask, render_template

app = Flask(__name__)

# / 경로로 접속하면 home() 함수가 실행됩니다.
@app.route('/')
def home():
    # debug 모드일 때만 호스트네임을 가져옵니다.
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    # render_template에 'computername' 인자로 호스트네임 변수를 전달합니다.
    return render_template('index.html', computername=hostname)

@app.route("/menu")
def menu():
    return render_template("menu.html")

# 이미 아래 코드가 있다면 중복 없이 두기
if __name__ == "__main__":  
    app.run(debug=True)
