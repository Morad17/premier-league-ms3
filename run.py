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
    detail = mongo.db.Team_Details.find()

    return render_template("landing-page.html", detail=detail)

###Club Links ( )#####
@app.route('/arsenal')
def arsenal():
    category = mongo.db.Team_Details.find({'club':'Arsenal FC'})
    details = mongo.db.Team_Details.find({'club':'Arsenal FC'})
    trophies = mongo.db.Trophies_Won.find({'club':'Arsenal FC'})
    players = mongo.db.Club_Players.find({'club':'Arsenal FC'})
    categories = list(mongo.db.Club_Categories.find())
    
    
    return render_template("arsenal.html", details=details, trophies=trophies, players=players, categories=categories, category=category)

@app.route('/aston_villa')
def aston_villa():
    details = mongo.db.Team_Details.find({'club':'Aston Villa'})
    trophies = mongo.db.Trophies_Won.find({'club':'Aston Villa'})
    players = mongo.db.Club_Players.find({'club':'Aston Villa'})
    
    return render_template("aston-villa.html", details=details , trophies=trophies, players=players )

@app.route('/bournemouth')
def bournemouth():
    details = mongo.db.Team_Details.find({'club':'AFC Bournemouth'})
    trophies = mongo.db.Trophies_Won.find({'club':'AFC Bournemouth'})
    players = mongo.db.Club_Players.find({'club':'AFC Bournemouth'})
    
    return render_template("aston-villa.html", details=details, trophies=trophies, players=players)

@app.route('/brighton')
def brighton():
    details = mongo.db.Team_Details.find({'club':'Brighton & Hove Albion'})
    trophies = mongo.db.Trophies_Won.find({'club':'Brighton & Hove Albion'})
    players = mongo.db.Club_Players.find({'club':'Brighton & Hove Albion'})
    
    return render_template("brighton.html", details=details, trophies=trophies, players=players)

@app.route('/burnley')
def burnley():
    details = mongo.db.Team_Details.find({'club':'Burnley'})
    trophies = mongo.db.Trophies_Won.find({'club':'Burnley'})
    players = mongo.db.Club_Players.find({'club':'Burnley'})
    
    return render_template("burnley.html", details=details, trophies=trophies, players=players)

@app.route('/chelsea')
def chelsea():
    details = mongo.db.Team_Details.find({'club':'Chelsea'})
    trophies = mongo.db.Trophies_Won.find({'club':'Chelsea'})
    players = mongo.db.Club_Players.find({'club':'Chelsea'})
    
    return render_template("chelsea.html", details=details, trophies=trophies, players=players)

@app.route('/crystal_palace')
def crystal_palace():
    details = mongo.db.Team_Details.find({'club':'Crystal Palace'})
    trophies = mongo.db.Trophies_Won.find({'club':'Crystal Palace'})
    players = mongo.db.Club_Players.find({'club':'Crystal Palace'})
    
    return render_template("crystal-palace.html", details=details, trophies=trophies, players=players)

@app.route('/everton')
def everton():
    details = mongo.db.Team_Details.find({'club':'Everton'})
    trophies = mongo.db.Trophies_Won.find({'club':'Everton'})
    players = mongo.db.Club_Players.find({'club':'Everton'})
    
    return render_template("everton.html", details=details, trophies=trophies, players=players)

@app.route('/leicester')
def leicester():
    details = mongo.db.Team_Details.find({'club':'Leicester City'})
    trophies = mongo.db.Trophies_Won.find({'club':'Leicester City'})
    players = mongo.db.Club_Players.find({'club':'Leicester City'})
    
    return render_template("leicester-city.html", details=details, trophies=trophies, players=players)

@app.route('/liverpool')
def liverpool():
    details = mongo.db.Team_Details.find({'club':'Liverpool'})
    trophies = mongo.db.Trophies_Won.find({'club':'Liverpool'})
    players = mongo.db.Club_Players.find({'club':'Liverpool'})
    
    return render_template("liverpool.html", details=details, trophies=trophies, players=players)

@app.route('/manchester_city')
def manchester_city():
    details = mongo.db.Team_Details.find({'club':'Manchester City'})
    trophies = mongo.db.Trophies_Won.find({'club':'Manchester City'})
    players = mongo.db.Club_Players.find({'club':'Manchester City'})
    
    return render_template("manchester-city.html", details=details, trophies=trophies, players=players)

@app.route('/manchester_united')
def manchester_united():
    details = mongo.db.Team_Details.find({'club':'Manchester United'})
    trophies = mongo.db.Trophies_Won.find({'club':'Manchester United'})
    players = mongo.db.Club_Players.find({'club':'Manchester United'})
    
    return render_template("manchester-united.html", details=details, trophies=trophies, players=players)

@app.route('/newcastle')
def newcastle():
    details = mongo.db.Team_Details.find({'club':'Newcastle United'})
    trophies = mongo.db.Trophies_Won.find({'club':'Newcastle United'})
    players = mongo.db.Club_Players.find({'club':'Newcastle United'})
    
    return render_template("newcastle.html", details=details, trophies=trophies, players=players)

@app.route('/norwhich')
def norwhich():
    details = mongo.db.Team_Details.find({'club':'Norwhich City'})
    trophies = mongo.db.Trophies_Won.find({'club':'Norwhich City'})
    players = mongo.db.Club_Players.find({'club':'Norwhich City'})
    
    return render_template("norwhich.html", details=details, trophies=trophies, players=players)

@app.route('/sheffield')
def sheffield():
    details = mongo.db.Team_Details.find({'club':'Sheffield United'})
    trophies = mongo.db.Trophies_Won.find({'club':'Sheffield United'})
    players = mongo.db.Club_Players.find({'club':'Sheffield United'})
    
    return render_template("sheffield.html", details=details, trophies=trophies, players=players)

@app.route('/southampton')
def southampton():
    details = mongo.db.Team_Details.find({'club':'Southampton'})
    trophies = mongo.db.Trophies_Won.find({'club':'Southampton'})
    
    
    return render_template("southampton.html", details=details, trophies=trophies, players=players)

@app.route('/spurs')
def spurs():
    details = mongo.db.Team_Details.find({'club':'Tottenham Hotspur'})
    trophies = mongo.db.Trophies_Won.find({'club':'Tottenham Hotspur'})
    
    return render_template("tottenham.html", details=details, trophies=trophies, players=players)

@app.route('/watford')
def watford():
    details = mongo.db.Team_Details.find({'club':'Watford'})
    trophies = mongo.db.Trophies_Won.find({'club':'Watford'})
    
    return render_template("watford.html", details=details, trophies=trophies, players=players)

@app.route('/west_ham')
def west_ham():
    details = mongo.db.Team_Details.find({'club':'West Ham United'})
    trophies = mongo.db.Trophies_Won.find({'club':'West Ham United'})
    
    return render_template("west-ham.html", details=details, trophies=trophies, players=players)

@app.route('/wolves')
def wolves():
    details = mongo.db.Team_Details.find({'club':'Wolverhampton Wanderers'})
    trophies = mongo.db.Trophies_Won.find({'club':'Wolverhampton Wanderers'})
    
    return render_template("wolves.html", details=details, trophies=trophies, players=players)


@app.route('/insert_club', methods=['POST'])
def insert_club():
    club = mongo.db.Team_Details
    club.insert_one(request.form.to_dict())
    return redirect(url_for('get_clubs'))

    return render_template("addclub.html", )

@app.route('/edit_club/<player_id>')
def edit_club(player_id): 
    player = mongo.db.Club_Players.find_one({"_id":ObjectId(player_id)})
    categories = list(mongo.db.Club_Categories.find())
    return render_template('editplayer.html', player=player, categories=categories)


@app.route('/update_player/<player_id>', methods=["POST"])
def update_club(player_id):
    player = mongo.db.Club_Players
    player.update(  {'_id': ObjectId(player_id)},
    {'player_club': request.form.get('club')},
    {'player_name': request.form.get('name')},
    {'player_position': request.form.get('position')},
    {'player_nationality': request.form.get('nationality')},
    {'player_number': request.form.get('number')}, {"upsert":False})

    return redirect(url_for('get_clubs'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

