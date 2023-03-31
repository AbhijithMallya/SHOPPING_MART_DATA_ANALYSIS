from flask import Blueprint, request
from sqlalchemy.sql import text
from db import db
import datetime

visitor_blueprint = Blueprint('visitor_blueprint', __name__)


@visitor_blueprint.route('/log-visitors', methods=['POST'])
def addVisitorData():
    gender = request.form['gender']
    ageGroup = request.form['age-group']
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    print(currentDate)
    currentTime = datetime.datetime.now().strftime("%H:%M:%S")
    sql = text('INSERT INTO visitors_log(visitor_gender,visitor_age,visitor_date,visitor_time) values(' +str(gender)+','+str(ageGroup)+',"'+currentDate+'","'+currentTime+'")')

    #Executing the query -- SQLAlchemy version (1.4.46)
    db.engine.execute(sql)
    
    return "Data Logged Successfully"
