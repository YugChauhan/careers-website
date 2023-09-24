from flask import Flask, render_template

app = Flask(__name__)

Jobs=[
  {
    "title":"Data Scientist",
    "location":"India, U.P.",
    "salary":"$20000"
  },
  {
    "title":"Data Analyst",
    "location":"India, M.P.",
    "salary":"$10000"
  },
  {
    "title":"Software Engineer",
    "location":"India, Karnataka",
    "salary":"$14000"
  }
]


@app.route("/")
def index_html():
    return render_template("index.html",jobs=Jobs)

app.run(host='0.0.0.0',debug=True)