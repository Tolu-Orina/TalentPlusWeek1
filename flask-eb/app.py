# Import necessary libraries
from flask import Flask, render_template
import requests

# Instantiate the application
app = Flask(__name__)



@app.route("/")
def hello():
    api_uri = "https://b2v35rtc3b.execute-api.us-east-1.amazonaws.com/"
    response = requests.get(api_uri)
    my_word = response.json()

    return render_template("index.html", my_word=my_word)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
