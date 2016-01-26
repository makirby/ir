from app import app, db
from app.models import team
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/teams', methods=['GET'])
def get_all_teams():
    entities = team.Team.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/teams/<int:id>', methods=['GET'])
def get_team(id):
    entity = team.Team.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/teams', methods=['POST'])
def create_team():
    entity = team.Team(
        name=request.json['name']
        , img_location=request.json['img_location']
        , icon_location=request.json['icon_location']
        , team_text=request.json['team_text']
        , ground_id=request.json['ground_id']
        , team_type=request.json['team_type']
        , established=datetime.datetime.strptime(request.json['established'], "%Y-%m-%d").date()
        , season_id=request.json['season_id']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/teams/<int:id>', methods=['PUT'])
def update_team(id):
    entity = team.Team.query.get(id)
    if not entity:
        abort(404)
    entity = team.Team(
        name=request.json['name'],
        img_location=request.json['img_location'],
        icon_location=request.json['icon_location'],
        team_text=request.json['team_text'],
        ground_id=request.json['ground_id'],
        team_type=request.json['team_type'],
        established=datetime.datetime.strptime(request.json['established'], "%Y-%m-%d").date(),
        season_id=request.json['season_id'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/teams/<int:id>', methods=['DELETE'])
def delete_team(id):
    entity = team.Team.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
