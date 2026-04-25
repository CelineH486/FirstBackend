from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://admin:123456@localhost:27017")

# 建立資料庫 & collection
db = client["calculator_db"]
collection = db["history"]



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    result = num1 + num2

    collection.insert_one({
    "num1": num1,
    "num2": num2,
    "op": "add",
    "result": result
})

    return jsonify({"result": result})


@app.route("/api/minus", methods=["POST"])
def minus():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    result = num1 - num2

    collection.insert_one({
    "num1": num1,
    "num2": num2,
    "op": "minus",
    "result": result
})

    return jsonify({"result": result})


@app.route("/api/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    result = num1 * num2

    collection.insert_one({
        "num1": num1,
        "num2": num2,
        "op": "multiply",
        "result": result
    })

    return jsonify({"result": result})


@app.route("/api/divide", methods=["POST"])
def divide():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])

    if num2 == 0:
        result = "不能除以0"
    else:
        result = num1 / num2

    collection.insert_one({
        "num1": num1,
        "num2": num2,
        "op": "divide",
        "result": result
    })

    return jsonify({"result": result})


@app.route("/api/history", methods=["GET"])
def get_history():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)