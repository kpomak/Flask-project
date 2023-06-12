from flask import Blueprint, jsonify, request

from newspapper.utils.bard import bard, translator


bard_app = Blueprint("bard_app", __name__)


@bard_app.route("/", methods=["GET"], endpoint="answer")
def answer():
    question = request.args.get("content")
    question = translator.translate(question)
    response = bard.get_answer(question.text)
    return jsonify(response)
