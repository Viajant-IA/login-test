from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import json
import os
import jwt
import http
import requests

app = Flask(__name__)

JSON_FILE = "login.json"

@app.route("/login")
def login():
    return render_template ("index.html")

# para erros HTTP
class HTTPError():
    errors = {
        404
    }

    if 404():
        print("Parece que deu um 404 aqui viu! Erro: {errors}")

