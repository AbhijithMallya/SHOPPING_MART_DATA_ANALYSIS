from flask import Flask ,render_template
from flask_cors  import CORS
from db import db
from visitor_log import visitor_blueprint
from dashboard import dashboard_blueprint



app=Flask(__name__)
CORS(app)

#Database Configuration
username="root"
password=""
userpass='mysql+pymysql://'+username+':'+password+'@'
server='127.0.0.1'
dbname='/wallmart_visitors'

app.config['SQLALCHEMY_DATABASE_URI']=userpass+server+dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)

#Regsiter Blueprints
app.register_blueprint(visitor_blueprint)   
app.register_blueprint(dashboard_blueprint)





#API End point - Route

@app.route('/')
def hello():
    return "Server Up. Hello world "



if __name__ =='__main__':
    app.debug=True
    app.run()
    