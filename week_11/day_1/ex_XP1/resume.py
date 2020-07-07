import flask

resume = flask.Flask(__name__)

@resume.route('/<company>')
def index(company):
    return flask.render_template('home.jin/index.html',company=company)

resume.run()
