from flask import Blueprint

test_blueprint = Blueprint('test', __name__)


@test_blueprint.route("/test")
def do_a_test():
    return "just a test"
