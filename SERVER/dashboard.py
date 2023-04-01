from flask import Blueprint, request , jsonify
from sqlalchemy.sql import text
from db import db
import datetime

dashboard_blueprint = Blueprint('dashboard_blueprint',__name__)

#Todays Visitors
@dashboard_blueprint.route('/today-visitors')
def todayVisitors():
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    sqlTodayVisitors=text( 'SELECT COUNT(*) AS today_visitors FROM visitors_log WHERE visitor_date= "'+currentDate+'"' )
    resultData = db.engine.execute(sqlTodayVisitors)
    rawData = resultData.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData


  


