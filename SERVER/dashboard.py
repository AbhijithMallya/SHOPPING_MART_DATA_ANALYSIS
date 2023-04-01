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



#Overall Visitors
@dashboard_blueprint.route('/overall-visitors')
def overallVisitors():
    sqlOverallVisitors=text('SELECT COUNT(id) as overall_visitors FROM visitors_log') 
    resultData = db.engine.execute(sqlOverallVisitors)
    rawData = resultData.fetchall()
    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData
 

 #Todays Male Visitors
@dashboard_blueprint.route('/male-visitors')
def maleVisitors():
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    sqlOverallVisitors=text('SELECT COUNT(*) as male_visitors FROM visitors_log where visitor_gender=1 and visitor_date="'+ currentDate+'"') 
    resultData = db.engine.execute(sqlOverallVisitors)
    rawData = resultData.fetchall()
    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData

#Todays Female Visitors
@dashboard_blueprint.route('/female-visitors')
def femaleVisitors():
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    sqlOverallVisitors=text('SELECT COUNT(*) as female_visitors FROM visitors_log where visitor_gender=2 and visitor_date="'+ currentDate+'"') 
    resultData = db.engine.execute(sqlOverallVisitors)
    rawData = resultData.fetchall()
    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData
 
 

#Table Data
@dashboard_blueprint.route('/table-data')
def tableData():
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    txtlabel=''
    x=''
    for a in range(1,6) :
        if a==1 :
            txtlabel='Kids'
        elif a==2 :
            txtlabel='Teenagers'
        elif a==3 :
            txtlabel='Youngsters'
        elif a==4 :
            txtlabel='Adults'
        elif a==5 :
            txtlabel='Seniors'
        
    
        for g in range(1,3):
            #Todays Visitors
            sqlTodayVisitors=text( 'SELECT COUNT(*) AS today_visitors FROM visitors_log WHERE visitor_date= "'+currentDate+'" AND visitor_gender = '+str(g)+' AND visitor_age='+str(a)+' ' )
            resultData = db.engine.execute(sqlTodayVisitors)
            rawData = resultData.fetchall()
            ageGroupGenderToday = rawData[0].today_visitors

            #Overall Visitors
            sqlOverallVisitors=text( 'SELECT COUNT(*) AS overall_visitors FROM visitors_log WHERE  visitor_gender = '+str(g)+' AND visitor_age='+str(a)+' ' )
            resultData = db.engine.execute(sqlOverallVisitors)
            rawData = resultData.fetchall()
            ageGroupGenderOverall = rawData[0].overall_visitors

            gText=''
            if g==1:
                gText='Male'
            elif g==2:
                gText='Female'
            x+= '{"gender":"'+gText+'","age_group":"'+txtlabel+'","today_visitors":"'+str(ageGroupGenderToday)+'","overall_visitors":"'+str(ageGroupGenderOverall)+'"},'
        #End of inner for loop
    #End of outer for loop
    x=x[:-1]
    #to remove the extra comma after last loop
    jsonData = ' ['+x+'] '
    return jsonData
        


#Graph
@dashboard_blueprint.route('/graph-data')
def graphData():
    x=''
    for m in range(1,13) :
        sqlMonthdata = text('SELECT COUNT(*) as monthly_visitors from visitors_log where month(visitor_date)="'+str(m)+'"  ' )
        resultData =  db.engine.execute(sqlMonthdata)
        rawData = resultData.fetchall()
        totalMonthlyVisitors = rawData[0].monthly_visitors
                                    # alias name in sql query
        x+= '{"month":"'+str(totalMonthlyVisitors)+'"},'
    x=x[:-1]
    #to remove the extra comma after last loop
    jsonData = '['+x+']'
    return jsonData

            
