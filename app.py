from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load(open("Prediksi Harga Rumah.jlb", "rb"))

@app.route("/")
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)