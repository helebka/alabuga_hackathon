import os

from flask import Flask, redirect
from dotenv import load_dotenv
from flask import request, render_template

from app.analysers.text_analyser import text_analyser
from app.get_web_data.parser import parser

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_get():
    return render_template("/main.html")


@app.route("/", methods=["POST"])
def index_post():
    url = request.form.get("inp")
    if not url:
        return redirect("/")
    if url[:4] == "http":
        text = parser(url)
    else:
        text = url
    
    answer = text_analyser(text)
    return render_template("/main.html", company=answer[0], mood=answer[1])
