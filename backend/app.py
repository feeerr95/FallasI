from flask_cors import CORS
from flask import Flask, request
from Robot3DTroubles import Robot3DTroubles
from Robot3DTroubles import Trouble
from rete import RETE


def errors():
    global errors


rete = RETE()
engine = Robot3DTroubles()

app = Flask(__name__)
CORS(app)


@app.route("/api/rete/firstQuestion/")
def get_first_question():
    userCondition = request.args.get('userCondition')
    (condition, question) = rete.get_first_question(userCondition)
    return {
        "nextCondition": condition,
        "nextQuestion": question
    }


@app.route("/api/rete/nextQuestion/")
def get_next_question():
    userCondition = request.args.get('userCondition')
    userResponse = request.args.get('userResponse')
    nextQuestion = rete.get_next_question(userCondition, userResponse)

    if(not nextQuestion):
        return {
            "result": rete.get_solution()
        }

    return {
        "nextCondition": nextQuestion[0],
        "nextQuestion": nextQuestion[1],
    }


@app.route("/api/trouble/")
def get_trouble():
    name = request.args.get('name')
    engine.reset()
    engine.declare(Trouble(error=name))
    engine.run()
    response = errors[0] if len(errors) == 1 else None
    newErrors = errors if len(errors) > 1 else []
    return {
        "response": response,
        "newErrors": newErrors
    }


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
