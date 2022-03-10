from flask import Flask,request
from textblob import TextBlob
app = Flask(__name__)

@app.route("/sentiment",methods=["POST","GET"])
def analyser():
    text = request.get_data()
    text=text.decode("utf-8")
    a = TextBlob(text)
    m = a.sentiment.polarity
    m += 1
    m *= 50
    return str(m)


if __name__ == '__main__':
    app.run(debug=True)
