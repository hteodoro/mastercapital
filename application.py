
from flask import Flask
from flask import render_template
from flask import url_for

application = Flask(__name__)

@application.route("/")
@application.route("/home")
def home():
    return render_template('index.html')

@application.route("/sobre")
def sobre():
    return render_template('sobre.html')

@application.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
    application.run()