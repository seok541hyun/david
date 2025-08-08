from flask import Flask, render_template

app = Flask(__name__)

@app.route("/menu")
def menu():
    return render_template("menu.html")

# 이미 아래 코드가 있다면 중복 없이 두기
if __name__ == "__main__":  
    app.run(debug=True)
