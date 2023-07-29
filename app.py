from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Flask"

@app.route('/cal', methods=["GET"])
def math_operator():
    operation = request.json["operation"]
    num1 = int(request.json["number1"])
    num2 = int(request.json["number2"])

    if operation == "add":
        result = num1 + num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "div":
        result = num1/num2
    else:
        result = num1 - num2
    return jsonify(result)


if __name__=="__main__":
    app.run()