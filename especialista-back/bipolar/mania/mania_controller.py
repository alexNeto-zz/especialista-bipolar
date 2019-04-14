from flask import Blueprint, request

from bipolar.mania.mania_model import ManiaModel

mania_blueprint = Blueprint(r'mania', __name__)


@mania_blueprint.route('/')
def mania_questions():
    return ManiaModel(request.args).resolve()
