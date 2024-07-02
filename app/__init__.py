import os
import requests

from flask import Flask
from dotenv import load_dotenv
from flask import request, jsonify, make_response, render_template

from app.analysers.text_analyser import text_analyser
from app.get_web_data.parser import parser

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():
    return render_template("/main.html")


@app.route("/", methods=["POST"])
def index_post():
    inp = request.form.get("inp")
    answer = requests.post("http://127.0.0.1:5000/post", json={"url": inp}).json()
    return render_template("/result.html")


@app.route("/post", methods=["POST"])
def post():
    date = request.get_json()
    url = date["url"]
    text = parser(url)
    answer = text_analyser(text)
    
    return make_response(jsonify(answer))

