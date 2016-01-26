from app import app, db
from app.models import player_team
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/player_teams', methods=['GET'])
def get_all_player_teams():

    entities = player_team.Player_team.query.all()

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/player_teams/<int:id>', methods=['GET'])
def get_player_team(id):

    entity = player_team.Player_team.query.get(id)

    if not entity:
        abort(404)

    return jsonify(entity.to_dict())


@app.route('/inforugby/player_teams', methods=['POST'])
def create_player_team():
    entity = player_team.Player_team(
        player_id=request.json['player_id']
        , team_id=request.json['team_id']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/player_teams/<int:id>', methods=['PUT'])
def update_player_team(id):
    entity = player_team.Player_team.query.get(id)
    if not entity:
        abort(404)
    entity = player_team.Player_team(
        player_id=request.json['player_id'],
        team_id=request.json['team_id'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/player_teams/<int:id>', methods=['DELETE'])
def delete_player_team(id):
    entity = player_team.Player_team.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
