from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def index():
    link = "<h1>歡迎進入鍾若筠的網站</h1>"
    link += "<a href =/mis>課程</a><hr>"
    link += "<a href =/today>現在日期時間</a><hr>"
    link += "<a href =/me>關於我</a><hr>"
    link += "<a href =/welcome?suga=鍾若筠&d=靜宜資管&c=>Get傳值</a><hr>"
    link += "<a href =/account>網頁表單傳值</a><br>"
    link += "<a href=/calc>次方與根號計算 (網頁表單傳值)</a><br>"
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href=/>返回首頁</a>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/me")
def me():
    return render_template("mis2026b.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("suga")
    d= request.values.get("d")
    c= request.values.get("c")
    return render_template("welcome.html", name=user,dep=d,course=c)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        # 這裡處理表單傳過來的數值
        x = float(request.form.get("x", 0))
        y = float(request.form.get("y", 0))
        op = request.form.get("op")
        
        if op == "pow":
            res = x ** y
            msg = f"{x} 的 {y} 次方為 {res}"
        else:
            res = x ** (1/y)
            msg = f"{x} 的 {y} 次方根為 {res}"
            
        return f"<h1>計算結果</h1><p>{msg}</p><a href='/calc'>重新計算</a>"
    
    # GET 請求時，顯示計算機畫面
    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)