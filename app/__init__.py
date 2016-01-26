from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


from app.models import competition
from app.models import competition_team
from app.models import team
from app.models import player_team
from app.models import match
from app.models import match_team
from app.models import event
from app.models import squad
from app.models import player
from app.routes import index

from app.routes import competitions
from app.routes import competition_teams
from app.routes import teams
from app.routes import player_teams
from app.routes import matches
from app.routes import match_teams
from app.routes import events
from app.routes import squads
from app.routes import players
