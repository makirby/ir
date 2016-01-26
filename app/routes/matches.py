from app import app, db
from app.models import match
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/matches', methods=['GET'])
def get_all_matches():
    entities = match.Match.query.all()

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/matches/<int:id>', methods=['GET'])
def get_match(id):
    entity = match.Match.query.get(id)

    if not entity:
        abort(404)

    return jsonify(entity.to_dict())


@app.route('/inforugby/matches', methods=['POST'])
def create_match():
    entity = match.Match(
        competition_id=request.json['competition_id']
        , home_match_team_id=request.json['home_match_team_id']
        , away_match_team_id=request.json['away_match_team_id']
        , match_text=request.json['match_text']
        , ground_id=request.json['ground_id']
        , home_score=request.json['home_score']
        , away_score=request.json['away_score']
        , img_location=request.json['img_location']
        , match_date=datetime.datetime.strptime(request.json['match_date'], "%Y-%m-%d").date()
        , match_outcome=request.json['match_outcome']
        , match_type=request.json['match_type']
    )

    db.session.add(entity)
    db.session.commit()

    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/matches/<int:id>', methods=['PUT'])
def update_match(id):
    entity = match.Match.query.get(id)

    if not entity:
        abort(404)

    entity = match.Match(
        competition_id=request.json['competition_id'],
        home_match_team_id=request.json['home_match_team_id'],
        away_match_team_id=request.json['away_match_team_id'],
        match_text=request.json['match_text'],
        ground_id=request.json['ground_id'],
        home_score=request.json['home_score'],
        away_score=request.json['away_score'],
        img_location=request.json['img_location'],
        match_date=datetime.datetime.strptime(request.json['match_date'], "%Y-%m-%d").date(),
        match_outcome=request.json['match_outcome'],
        match_type=request.json['match_type'],
        id=id
    )

    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/matches/<int:id>', methods=['DELETE'])
def delete_match(id):
    entity = match.Match.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
