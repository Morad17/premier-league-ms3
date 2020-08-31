import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'premierLeague'
app.config["MONGO_URI"] = 'mongodb+srv://root:London20@myfirstcluster-ay9fk.mongodb.net/premierLeague?retryWrites=true&w=majority'

mongo = PyMongo(app)

###User Landing Page####
@app.route('/')
@app.route('/get_clubs')
def get_clubs():
    """user chooses which club to view"""
    detail = mongo.db.Team_Details.find()

    return render_template("landing-page.html", detail=detail)


####User Login####
@app.route('/<username>')
def user(username):
    return


###Club Links ( )#####
@app.route('/arsenal')
def arsenal():
    details = mongo.db.Team_Details.find({'club':'Arsenal FC'})
    trophies = mongo.db.Trophies_Won.find({'club':'Arsenal FC'})
    players = mongo.db.Club_Players.find({'club':'Arsenal FC'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players,)

@app.route('/aston_villa')
def aston_villa():
    details = mongo.db.Team_Details.find({'club':'Aston Villa'})
    trophies = mongo.db.Trophies_Won.find({'club':'Aston Villa'})
    players = mongo.db.Club_Players.find({'club':'Aston Villa'})
    
    return render_template("team.html", details=details , trophies=trophies, players=players )

@app.route('/bournemouth')
def bournemouth():
    details = mongo.db.Team_Details.find({'club':'AFC Bournemouth'})
    trophies = mongo.db.Trophies_Won.find({'club':'AFC Bournemouth'})
    players = mongo.db.Club_Players.find({'club':'AFC Bournemouth'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/brighton')
def brighton():
    details = mongo.db.Team_Details.find({'club':'Brighton & Hove Albion'})
    trophies = mongo.db.Trophies_Won.find({'club':'Brighton & Hove Albion'})
    players = mongo.db.Club_Players.find({'club':'Brighton & Hove Albion'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/burnley')
def burnley():
    details = mongo.db.Team_Details.find({'club':'Burnley'})
    trophies = mongo.db.Trophies_Won.find({'club':'Burnley'})
    players = mongo.db.Club_Players.find({'club':'Burnley'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/chelsea')
def chelsea():
    details = mongo.db.Team_Details.find({'club':'Chelsea'})
    trophies = mongo.db.Trophies_Won.find({'club':'Chelsea'})
    players = mongo.db.Club_Players.find({'club':'Chelsea'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/crystal_palace')
def crystal_palace():
    details = mongo.db.Team_Details.find({'club':'Crystal Palace'})
    trophies = mongo.db.Trophies_Won.find({'club':'Crystal Palace'})
    players = mongo.db.Club_Players.find({'club':'Crystal Palace'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/everton')
def everton():
    details = mongo.db.Team_Details.find({'club':'Everton'})
    trophies = mongo.db.Trophies_Won.find({'club':'Everton'})
    players = mongo.db.Club_Players.find({'club':'Everton'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/leicester')
def leicester():
    details = mongo.db.Team_Details.find({'club':'Leicester City'})
    trophies = mongo.db.Trophies_Won.find({'club':'Leicester City'})
    players = mongo.db.Club_Players.find({'club':'Leicester City'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/liverpool')
def liverpool():
    details = mongo.db.Team_Details.find({'club':'Liverpool'})
    trophies = mongo.db.Trophies_Won.find({'club':'Liverpool'})
    players = mongo.db.Club_Players.find({'club':'Liverpool'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/manchester_city')
def manchester_city():
    details = mongo.db.Team_Details.find({'club':'Manchester City'})
    trophies = mongo.db.Trophies_Won.find({'club':'Manchester City'})
    players = mongo.db.Club_Players.find({'club':'Manchester City'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/manchester_united')
def manchester_united():
    details = mongo.db.Team_Details.find({'club':'Manchester United'})
    trophies = mongo.db.Trophies_Won.find({'club':'Manchester United'})
    players = mongo.db.Club_Players.find({'club':'Manchester United'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/newcastle')
def newcastle():
    details = mongo.db.Team_Details.find({'club':'Newcastle United'})
    trophies = mongo.db.Trophies_Won.find({'club':'Newcastle United'})
    players = mongo.db.Club_Players.find({'club':'Newcastle United'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/norwhich')
def norwhich():
    details = mongo.db.Team_Details.find({'club':'Norwhich City'})
    trophies = mongo.db.Trophies_Won.find({'club':'Norwhich City'})
    players = mongo.db.Club_Players.find({'club':'Norwhich City'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/sheffield')
def sheffield():
    details = mongo.db.Team_Details.find({'club':'Sheffield United'})
    trophies = mongo.db.Trophies_Won.find({'club':'Sheffield United'})
    players = mongo.db.Club_Players.find({'club':'Sheffield United'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/southampton')
def southampton():
    details = mongo.db.Team_Details.find({'club':'Southampton'})
    trophies = mongo.db.Trophies_Won.find({'club':'Southampton'})
    players = mongo.db.Club_Players.find({'club':'Southampton'})
    
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/spurs')
def spurs():
    details = mongo.db.Team_Details.find({'club':'Tottenham Hotspur'})
    trophies = mongo.db.Trophies_Won.find({'club':'Tottenham Hotspur'})
    players = mongo.db.Club_Players.find({'club':'Tottenham Hotspur'})
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/watford')
def watford():
    details = mongo.db.Team_Details.find({'club':'Watford'})
    trophies = mongo.db.Trophies_Won.find({'club':'Watford'})
    players = mongo.db.Club_Players.find({'club':'Watford'})
    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/west_ham')
def west_ham():
    details = mongo.db.Team_Details.find({'club':'West Ham United'})
    trophies = mongo.db.Trophies_Won.find({'club':'West Ham United'})
    players = mongo.db.Club_Players.find({'club':'West Ham United'})

    return render_template("team.html", details=details, trophies=trophies, players=players)

@app.route('/wolves')
def wolves():
    details = mongo.db.Team_Details.find({'club':'Wolverhampton Wanderers'})
    trophies = mongo.db.Trophies_Won.find({'club':'Wolverhampton Wanderers'})
    players = mongo.db.Club_Players.find({'club':'Wolverhampton Wanderers'})

    return render_template("team.html", details=details, trophies=trophies, players=players)

"""CRUD Functions"""

#Adding players #

@app.route('/add_player')
def add_player():
    """form to add new player(s) to db"""
    clubs = list(mongo.db.Clubs.find())
    return render_template("addplayer.html", clubs=clubs)

@app.route('/insert_player', methods=['POST'])
def insert_player():
     
    player = mongo.db.Club_Players
    player.insert_one(request.form.to_dict())
    return redirect(url_for('get_clubs'))

###Updating Player Info#####
@app.route('/edit_player/<player_id>')
def edit_player(player_id): 
    player = mongo.db.Club_Players.find_one({"_id":ObjectId(player_id)})
    categories = list(mongo.db.Club_Categories.find())
    return render_template('editplayer.html', player=player, categories=categories)



@app.route('/update_player/<player_id>', methods=["POST"])
def update_player(player_id):
    """change a player details in db"""
    player = mongo.db.Club_Players
    player.update(  {'_id': ObjectId(player_id)},
    {'club': request.form.get('player_club'),
    'name': request.form.get('player_name'),
    'position': request.form.get('player_position'),
    'nationality': request.form.get('player_nationality'),
    'number': request.form.get('player_number')})

    return redirect(url_for('get_clubs'))
######Delete Player####

@app.route('/delete_player/<player_id>')
def delete_player(player_id):
    """deletes player"""
    mongo.db.Club_Players.remove({"_id":ObjectId(player_id)})
    return redirect(url_for('get_clubs'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

