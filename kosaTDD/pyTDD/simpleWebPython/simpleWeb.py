####################################################################################################
# 필요한 모듈 import, 기본 설정
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import time

# 웹 서버 만들기
app = Flask(__name__, static_folder='public', template_folder='template')
app.secret_key = 'ApacheJMeter_TestWeb_Secret_Key_#2023#'

####################################################################################################
# 환경 설정 변수 밍 사용자 정보
DEBUG_MODE = True
users = {
    "user": "password",
    "user0": "password0",
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}

####################################################################################################
# 공통 함수
# 로그인이 필요한 페이지에서 호출되는 함수
def login_required(func):
    def wrapper(*args, **kwargs):
        if session.get("logged_in"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper


####################################################################################################
# 라우터
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password.")
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("username", None)
    return redirect(url_for("index"))

# /add는 로그인이 필요한 페이지.
@app.route("/add")
@login_required
def add():
    # GET 파라미터가 없으면 add.html을 랜더링
    num1 = request.args.get("num1", None)
    num2 = request.args.get("num2", None)
    if num1 is None or num2 is None:
        return render_template("add.html")
 
    # 결과를 HTML 템플릿에 전달합니다.
    result = int(num1) + int(num2)
    return render_template("add_result.html", num1=num1, num2=num2, result=result)

# WebAPI : json POST로 개수를 전달받아 개수만큼 랜덤 숫자를 생성하여 json으로 리턴
# curl -X POST -H "Content-Type: application/json" -d '{"count": 2}' http://127.0.0.1:7070/random
@app.route("/random", methods=["POST"])
def randomNumber():
    count = None
    try:
        count = request.json['count']
    except:
        pass
    if count is None:
        return jsonify([])
    
    random_numbers = {f'num{i}' : random.randint(0,1000) for i in range(count)}
    return jsonify(random_numbers)

# WebAPI : get parmeter로 전달된 데이터를 echo
# curl http://127.0.0.1:7070/echo?msg=hello
@app.route("/echo")
def echo():
    msg = request.args.get("msg", None)
    if msg is None:
        return "msg is None"
    return msg

# WebAPI : 임의의 시간동안 지연 후 응답
# curl http://127.0.0.1:7070/delay
@app.route("/delay")
def delay():
    delay = random.randint(0, 101) / 100
    time.sleep(delay)
    return f"{delay} delayed"

####################################################################################################
# Flask App Starting
if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=7070,
    debug=DEBUG_MODE)