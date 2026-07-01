from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("saved-model.pickle", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["A1"]),
        float(request.form["A2"]),
        float(request.form["A3"]),
        float(request.form["A4"]),
        float(request.form["A5"]),
        float(request.form["A6"]),
        float(request.form["A7"]),
        float(request.form["A8"]),
        float(request.form["A9"]),
        float(request.form["A10"]),
        float(request.form["A11"]),
        float(request.form["A12"]),
        float(request.form["A13"]),
        float(request.form["A14"]),
    ]

    prediction = model.predict([features])[0]

    if prediction == 1:
        result = "Approved"
    else:
        result = "Rejected"

    return render_template(
        "index.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)