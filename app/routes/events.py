from app import app, db
from app.models import event
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/events', methods=['GET'])
def get_all_events():
    entities = event.Event.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/events/<int:id>', methods=['GET'])
def get_event(id):
    entity = event.Event.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/events', methods=['POST'])
def create_event():
    entity = event.Event(
        event_type=request.json['event_type']
        , minute=request.json['minute']
        , player_id=request.json['player_id']
        , match_team_id=request.json['match_team_id']
        , event_text=request.json['event_text']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/events/<int:id>', methods=['PUT'])
def update_event(id):
    entity = event.Event.query.get(id)
    if not entity:
        abort(404)
    entity = event.Event(
        event_type=request.json['event_type'],
        minute=request.json['minute'],
        player_id=request.json['player_id'],
        match_team_id=request.json['match_team_id'],
        event_text=request.json['event_text'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    entity = event.Event.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
