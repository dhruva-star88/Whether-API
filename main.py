from flask import Flask, render_template
import pandas as pd

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
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temp = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "Temperature": temp
    }


if __name__ == "__main__":
    app.run(debug=True)
