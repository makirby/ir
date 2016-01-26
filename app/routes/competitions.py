from app import app, db
from app.models import competition
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/competitions', methods=['GET'])
def get_all_competitions():
    entities = competition.Competition.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/competitions/<int:id>', methods=['GET'])
def get_competition(id):
    entity = competition.Competition.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/competitions', methods=['POST'])
def create_competition():
    entity = competition.Competition(
        name=request.json['name']
        , competition_text=request.json['competition_text']
        , img_location=request.json['img_location']
        , icon_location=request.json['icon_location']
        , competition_type=request.json['competition_type']
        , created=datetime.datetime.strptime(request.json['created'], "%Y-%m-%d").date()
        , user_created=request.json['user_created']
        , season_id=request.json['season_id']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/competitions/<int:id>', methods=['PUT'])
def update_competition(id):
    entity = competition.Competition.query.get(id)
    if not entity:
        abort(404)
    entity = competition.Competition(
        name=request.json['name'],
        competition_text=request.json['competition_text'],
        img_location=request.json['img_location'],
        icon_location=request.json['icon_location'],
        competition_type=request.json['competition_type'],
        created=datetime.datetime.strptime(request.json['created'], "%Y-%m-%d").date(),
        user_created=request.json['user_created'],
        season_id=request.json['season_id'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/competitions/<int:id>', methods=['DELETE'])
def delete_competition(id):
    entity = competition.Competition.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
