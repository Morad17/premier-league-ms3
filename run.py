import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'premierLeague'
app.config["MONGO_URI"] = 'mongodb+srv://root:London20@myfirstcluster-ay9fk.mongodb.net/premierLeague?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_clubs')
def get_clubs():
    return render_template("landing-page.html")


@app.route('/arsenal')
def arsenal():
    details = mongo.db.Team_Details.find({'team_name':'Arsenal FC'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Arsenal FC'})
    
    return render_template("arsenal.html",details=details, trophies=trophies)

@app.route('/aston_villa')

def aston_villa():
    details = mongo.db.Team_Details.find({'team_name':'Aston Villa'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Aston Villa'})
    
    return render_template("aston-villa.html", details=details, trophies=trophies)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

