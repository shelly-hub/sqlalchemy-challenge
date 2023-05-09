import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
# #################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# # reflect an existing database into a new model
Base = automap_base()
# # reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement= Base.classes.measurement
Station = Base.classes.station

# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__)

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Measurement data"""
    # Query precipitation data
    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_ppt = []
    for date, prcp in results:
        ppt_dict = {}
        ppt_dict["date"] = date
        ppt_dict["prcp"] = prcp
        all_ppt.append(ppt_dict)

    return jsonify(all_ppt)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations data"""
    # Query all stations data
    results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    all_stations = []
    for name, station,latitude, longitude, elevation in results:
        station_dict = {}
        station_dict["name"] = name
        station_dict["station"] = station
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query temperature
    #  most-active station for the previous year of data.
    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
                filter(Measurement.station== "USC00519281").\
                filter(Measurement.date >= '2016-08-23').\
                filter(Measurement.date <= '2017-08-23').all()
                
    session.close()

    # Convert list of tuples into normal list
    all_temp = []
    for station, date, tobs in results:
        temp_dict = {}
        temp_dict["station"] = station
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_temp.append(temp_dict)

    return jsonify(all_temp)


@app.route("/api/v1.0/<start>")
def ss(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query for start date input
    results = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start ).all()
            
    session.close
    
    al = []
    for tavg, tmin, tmax in results:
        tempe_dict = {}
        tempe_dict["avg_tobs"] = tavg
        tempe_dict["min_tobs"] = tmin
        tempe_dict["max_tobs"] = tmax
        al.append(tempe_dict)

    return jsonify(al)

@app.route("/api/v1.0/<start>/<end>")
def ee(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query for start and end date input
    results = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start ).\
                filter(Measurement.date <= end ).all()
            
    session.close
    
    al = []
    for tavg, tmin, tmax in results:
        tempe_dict = {}
        tempe_dict["avg_tobs"] = tavg
        tempe_dict["min_tobs"] = tmin
        tempe_dict["max_tobs"] = tmax
        al.append(tempe_dict)

    return jsonify(al)
 
   
if __name__ == '__main__':
    app.run(debug=True)
