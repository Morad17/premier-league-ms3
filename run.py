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


    return render_template("landing-page.html", )

###Club Links#####
@app.route('/arsenal')
def arsenal():
    details = mongo.db.Team_Details.find({'team_name':'Arsenal FC'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Arsenal FC'})
    
    return render_template("arsenal.html", details=details , trophies=trophies )

@app.route('/aston_villa')
def aston_villa():
    details = mongo.db.Team_Details.find({'team_name':'Aston Villa'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Aston Villa'})
    
    return render_template("aston-villa.html", details=details , trophies=trophies )

@app.route('/bournemouth')
def bournemouth():
    details = mongo.db.Team_Details.find({'team_name':'AFC Bournemouth'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'AFC Bournemouth'})
    
    return render_template("aston-villa.html", details=details, trophies=trophies)

@app.route('/brighton')
def brighton():
    details = mongo.db.Team_Details.find({'team_name':'Brighton & Hove Albion'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Brighton & Hove Albion'})
    
    return render_template("brighton.html", details=details, trophies=trophies)

@app.route('/burnley')
def burnley():
    details = mongo.db.Team_Details.find({'team_name':'Burnley'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Burnley'})
    
    return render_template("burnley.html", details=details, trophies=trophies)

@app.route('/chelsea')
def chelsea():
    details = mongo.db.Team_Details.find({'team_name':'Chelsea'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Chelsea'})
    
    return render_template("chelsea.html", details=details, trophies=trophies)

@app.route('/crystal_palace')
def crystal_palace():
    details = mongo.db.Team_Details.find({'team_name':'Crystal Palace'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Crystal Palace'})
    
    return render_template("crystal-palace.html", details=details, trophies=trophies)

@app.route('/everton')
def everton():
    details = mongo.db.Team_Details.find({'team_name':'Everton'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Everton'})
    
    return render_template("everton.html", details=details, trophies=trophies)

@app.route('/leicester')
def leicester():
    details = mongo.db.Team_Details.find({'team_name':'Leicester City'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Leicester City'})
    
    return render_template("leicester-city.html", details=details, trophies=trophies)

@app.route('/liverpool')
def liverpool():
    details = mongo.db.Team_Details.find({'team_name':'Liverpool'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Liverpool'})
    
    return render_template("liverpool.html", details=details, trophies=trophies)

@app.route('/manchester_city')
def manchester_city():
    details = mongo.db.Team_Details.find({'team_name':'Manchester City'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Manchester City'})
    
    return render_template("manchester-city.html", details=details, trophies=trophies)

@app.route('/manchester_united')
def manchester_united():
    details = mongo.db.Team_Details.find({'team_name':'Manchester United'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Manchester United'})
    
    return render_template("manchester-united.html", details=details, trophies=trophies)

@app.route('/newcastle')
def newcastle():
    details = mongo.db.Team_Details.find({'team_name':'Newcastle United'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Newcastle United'})
    
    return render_template("newcastle.html", details=details, trophies=trophies)

@app.route('/norwhich')
def norwhich():
    details = mongo.db.Team_Details.find({'team_name':'Norwhich City'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Norwhich City'})
    
    return render_template("norwhich.html", details=details, trophies=trophies)

@app.route('/sheffield')
def sheffield():
    details = mongo.db.Team_Details.find({'team_name':'Sheffield United'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Sheffield United'})
    
    return render_template("sheffield.html", details=details, trophies=trophies)

@app.route('/southampton')
def southampton():
    details = mongo.db.Team_Details.find({'team_name':'Southampton'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Southampton'})
    
    return render_template("southampton.html", details=details, trophies=trophies)

@app.route('/spurs')
def spurs():
    details = mongo.db.Team_Details.find({'team_name':'Tottenham Hotspur'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Tottenham Hotspur'})
    
    return render_template("tottenham.html", details=details, trophies=trophies)

@app.route('/watford')
def watford():
    details = mongo.db.Team_Details.find({'team_name':'Watford'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Watford'})
    
    return render_template("watford.html", details=details, trophies=trophies)

@app.route('/west_ham')
def west_ham():
    details = mongo.db.Team_Details.find({'team_name':'West Ham United'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'West Ham United'})
    
    return render_template("west-ham.html", details=details, trophies=trophies)

@app.route('/wolves')
def wolves():
    details = mongo.db.Team_Details.find({'team_name':'Wolverhampton Wanderers'})
    trophies = mongo.db.Trophies_Won.find({'team_name':'Wolverhampton Wanderers'})
    
    return render_template("wolves.html", details=details, trophies=trophies)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

