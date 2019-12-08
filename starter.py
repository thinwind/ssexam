"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from app.app import create_app

app = create_app(environment='development')


@app.route('/', methods=['GET'], strict_slashes=False)
def lin_slogan():
    return """ssexam"""


if __name__ == '__main__':
    app.run(debug=True)
