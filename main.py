from flask import Flask, render_template

app = Flask(__name__)


# Decorator, which decorates the below function
@app.route("/")
def home():
    return render_template("home.html")


"""
<> represents the dynamic value can be added 
"""


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temp = 23
    return {
        "station": station,
        "date": date,
        "Temperature": temp
    }


if __name__ == "__main__":
    app.run(debug=True)
