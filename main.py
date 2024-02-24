from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


# Decorator, which decorates the below function
@app.route("/")
def home():
    # renders html page and sends station data to webpage
    return render_template("home.html", data=stations.to_html())


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


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # converts dataframe to dictionary
    result = df.to_dict(orient="records")
    return result


"""
In the following url we added year as subdirectory so that it wont clash with the second url
"""


@app.route("/api/v1/year/<station>/<year>")
def year_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str)
    result = df.loc[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
