# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(autoload_with = engine)

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route('/api/v1.0/precipitation')
def prcp():
    # Query measurement for dates and prcps
    date_prcp = session.query(measurement.date, measurement.prcp)
    session.close()

    # Create dict for dates & prcps
    dps = []
    for date, prcp in date_prcp:
        dp_dict = {}
        dp_dict[date] = prcp
        dps.append(dp_dict)

    return jsonify(dps)
    
@app.route('/api/v1.0/stations')
def stations():
    # Query stations
    station_list = []
    stations = session.query(station.station)
    session.close()

    for station in stations:
        station_list.append(station)
    
    return(station_list)

'''@app.route('/api/v1.0/tobs')
def tobs():'''