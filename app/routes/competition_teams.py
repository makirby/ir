from app import app, db
from app.models import competition_team
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/competition_teams', methods=['GET'])
def get_all_competition_teams():
    entities = competition_team.Competition_team.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/competition_teams/<int:id>', methods=['GET'])
def get_competition_team(id):
    entity = competition_team.Competition_team.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/competition_teams', methods=['POST'])
def create_competition_team():
    entity = competition_team.Competition_team(
        competition_id=request.json['competition_id']
        , team_id=request.json['team_id']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/competition_teams/<int:id>', methods=['PUT'])
def update_competition_team(id):
    entity = competition_team.Competition_team.query.get(id)
    if not entity:
        abort(404)
    entity = competition_team.Competition_team(
        competition_id=request.json['competition_id'],
        team_id=request.json['team_id'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/competition_teams/<int:id>', methods=['DELETE'])
def delete_competition_team(id):
    entity = competition_team.Competition_team.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
