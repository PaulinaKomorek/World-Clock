from datetime import datetime, timedelta
from time import gmtime, strftime
from flask import Flask

app=Flask(__name__)
city_time={"london": 0, "new york": -4, "warsaw": +1, "moscow": +3, "tokyo": +9 }

@app.route("/", methods=["get"])
def world_time():
    current_time=datetime.now()
    s=""
    for i in city_time:
        current_time_city= current_time + timedelta(hours=city_time[i] - int(strftime("%z", gmtime()))/100)
        s=s+i+ ": " + current_time_city.strftime("%H:%M:%S") +"<br/>"
    return s

@app.route("/<city>", methods=["get"])
def world_time_city(city):
    current_time=datetime.now()
    current_time_city= current_time + timedelta(hours=city_time[city]- int(strftime("%z", gmtime()))/100)
    s=current_time_city.strftime("%H:%M:%S")
    return s