
from flask import Flask


app = Flask(__name__)

@app.route('/')

def home():

    return "Bienvenue dans notre projet CI/CD avec Flask !"


if __name__ == "__main__":

    app.run(debug=True)
