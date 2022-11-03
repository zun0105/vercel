from flask import Flask, render_template, request
from datetime import datetime



app = Flask(__name__)


@app.route("/")
def index():
    homepage = "<h1>資管二B 411017551 邱梓綸的求職相關資訊</h1>"
    homepage += "<a href=/aboutnutty>MIS個人介紹</a><br><br>"
    homepage += "<a href=/job>職涯測驗</a><br><br>"
    homepage += "<a href=/work>工作介紹</a><br><br>"
    homepage += "<a href=/plan>求職履歷自傳</a><br><br>"
    return homepage


@app.route("/aboutnutty")
def aboutnutty(): 
    return render_template ("aboutnutty.html")

@app.route("/work")
def work(): 
    return render_template ("work.html")

@app.route("/job")
def job(): 
   return render_template("job.html")

@app.route("/plan")
def plan(): 
   return render_template("plan.html")


if __name__ == "__main__":
    app.run()
