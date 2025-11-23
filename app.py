from flask import Flask, request, jsonify
app = Flask(__name__)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.json
    bmi_value = calculate_bmi(data["weight"], data["height"])
    return jsonify({"bmi": bmi_value})