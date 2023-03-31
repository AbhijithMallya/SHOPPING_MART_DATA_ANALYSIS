from flask import Flask
from db import db
app=Flask(__name__)

#Database Configuration
username="root"
password=""
userpass='mysql+pymysql://'+username+':'+password+'@'
server='127.0.0.1'
dbname='/wallmart_visitors'

app.config['SQLALCHEMY_DATABASE_URI']=userpass+server+dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)

#API End point - Route
@app.route('/')
def hello():
    return '    Hello World!'


if __name__ =='__main__':
    app.debug=True
    app.run()
    