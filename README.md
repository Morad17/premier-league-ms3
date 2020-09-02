# Premier League

This project was designed for people into football and not into football alike. For footballing fans they can keep up to date with the latests player transfers, can edit and update their
details, and laso get background information of all the clubs in the premier league. However this is also for people that dont keep up to date with football, but want to be included
in footballing conversations! useing this website they can quickle look up any club, have access to all their info, and importanltly before a game find out the clubs first team.

## UX

This website has users in mind each step of the way. When first accessing the web page it clearly has instructions at the start on what to do, and has all clubs displayed in cards at
the bottom. also the nav helps to quickly access different clubs if they are in one club page and want to go to another. they can also click add player to create a player for a club.
The ux of the players side provides two buttons to edit and delete a player, which is usefull if the player leaves the league, or if they transfer to a different club in the premier league
and can be updated. The information has been clearly presented and a siple layout has been used to not alienate people who know nothing about football.

### User Stories

### first time user

1. As a first time user, I want a simple navigation system to access the particular information I wasnt
2. As a first time user, I would like a landing page that I can access on the fly to get me to the right information
3. As a first time userm I would like to receive instructions on the processes so I dont get stuck on anything
4. As a first time user I would like the current seasons information, that is up to date and current

### returning user

1. As a returning user, I would like to know that all the team background info is up to date
2. As a returning user, I would like to be able to change the players info as transfers during the season happen
3. As a returning user, I would like to update the database when a new player has been bought from a different league
4. As a returning user, I would like to delete players that have left a certain club, in the season
5. As a returning user, I would like to be able to quickly change clubs instead of always going to the landing page.

### Wireframe
A wireframe has been made with [figma](https://www.figma.com/file/8CkpJqSrwkKyawUokXX3XQ/P-L-Database).
To highlight the responsivness of the website this image shows the different resolutions ![Image](https://github.com/Morad17/premier-league-ms3/tree/master/static/responsive-design/responsive.png'). Also the offical Premier League website has been used as inspiration
for the layout of the page.


## Features

### Multi Navigation
The landing page allows the user to view all the clubs at once, and click on the club that they would like to go to. Also when in the club page they can click on the drop-down and select any of the other club
pages that they would like to visit.

Also in the dropdown each Club Name when hovered over changes color based on the actual clubs offical color. This is visually peasing and helps to associate the correct color with the club.

## Add player
The Add Player page has been made very simple and with instruction so that even tech illiterate people can operate it. Also when an entry has been selected it changes color to notify the user that
text has been written in the specified field.


### Edit button
The Edit Button when pressed directs the user to a page where they can change any of the players details, such as player position. To stop the user from going to and from pages, the 
current details of the user is already displayed, so they know what they already are. clubs are listed as a dropdown, to prevent any typo's or abbreviations of the club, which would stop
the player from appearing in the page

## Delete Player
The delete player simply deletes the current field of player and their details.

## Technologies used

### Pymongo and Flask
Python, Mongo and Flask have been used to allow for stored information to be manipulated. Mongodb is the database used where users inputs and current inputs will be stored, and by routeing via 
python and flask allows for the webpage to be interactive and to use the CRUD functions.So that the user can create, read update and delete any player in the premeir league. Bootstrap framework has been used to create a simple and responsive design, so users on mobile will have just as
good experience as computer users.

Other Technologies used:

### Front-end

1. Html
2. css
3. Javascript

### Back-end

1.Python
2.Mongodb

### Frameworks

1.Flask
2.Jinja
3.Bootstrap

## Testing

### User Stories
User Goal | Outcome
----------|---------
I would like a design where I can locate the Club I need to find information from | The langing page allows me to acces all the clubs, and the dropdown lets me go to another in quick succession
I would like to manipulate the data as the season goes to get the latest player info in each club | The table of players can be edited and deleted , and you can click add player to create a new player
I would like to see background information on the clubs that players play in | When clicking on the club all current background information is displayer

### General Testing 

"When clicking on club link the trophy icon is too large and overlaps with the number"
I have fixed this error with media queries to make sure no info is overlapping 

"The submit button on add player wasnt working"
I have changed the label and input order as it was blocking input from the user

"The screen is black and It come with a weird error"
The key value pair needed upated to reflect the same on the gitpod, which after many tests was found out and updated

### Responsive design

Care was taken to make the page 'user friendly' on all devices, the man resolutions that were tested were:
1. 'Iphone 6/7/8'
2. 'Ipad / Ipad Pro'
3. Standard Computer resolution

## Deployment

The app was deployed on Heroku, using the European server. The process to deploy on Heroku includes:
1. Creating a Heroku account, and making a new app
2. Loggin into Heroku on Gitpod and creating an origin to the Heroku app so that info can be commited to it
3. Making sure the environment variables matched the ones on gitpod, which are IP: 0.0.0.0 and PORT: 8080. 
4. Also adding the procfile and the requirements.txt to understand which installations are running on the project.

## Credits

A few Tutorials have been used to aid with the projects. The Youtube channels that I have used to help out include:
1. [Dev Ed](https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q) Heleped with the css designs
2. [Julian Nash](https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA) Helped with understanding more about routing in pymongo.
Also information has been used from these web pages:
1. css-tricks.com, used for css skills
2. premierleague.com/, used for info on players
3. wikipeadia also used for knowledgue on the background of clubs

### Media

The media in this site, incluiding club crests and images are property of fifa and have been used for information purposes only
Information from this site has been reached from premierleague.com and wikipedia. My icons are from fontawesome.com