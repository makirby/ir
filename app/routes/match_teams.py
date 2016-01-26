from app import app, db
from app.models import match_team
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/match_teams', methods=['GET'])
def get_all_match_teams():
    entities = match_team.Match_team.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/match_teams/<int:id>', methods=['GET'])
def get_match_team(id):
    entity = match_team.Match_team.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/match_teams', methods=['POST'])
def create_match_team():
    entity = match_team.Match_team(
        match_id=request.json['match_id']
        , team_id=request.json['team_id']
        , squad_id=request.json['squad_id']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/match_teams/<int:id>', methods=['PUT'])
def update_match_team(id):
    entity = match_team.Match_team.query.get(id)
    if not entity:
        abort(404)
    entity = match_team.Match_team(
        match_id=request.json['match_id'],
        team_id=request.json['team_id'],
        squad_id=request.json['squad_id'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/match_teams/<int:id>', methods=['DELETE'])
def delete_match_team(id):
    entity = match_team.Match_team.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
