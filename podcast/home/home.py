from flask import Blueprint, render_template

import podcast.utilities.utilities as utilities

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html'
    )

# TODO: Implement home() blueprint
