from app import app, db
from app.models import squad
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/squads', methods=['GET'])
def get_all_squads():
    entities = squad.Squad.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/squads/<int:id>', methods=['GET'])
def get_squad(id):
    entity = squad.Squad.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/squads', methods=['POST'])
def create_squad():
    entity = squad.Squad(
        tighthead_id=request.json['tighthead_id']
        , loosehead_id=request.json['loosehead_id']
        , hooker_id=request.json['hooker_id']
        , lock_4_id=request.json['lock_4_id']
        , lock_5_id=request.json['lock_5_id']
        , flanker_6_id=request.json['flanker_6_id']
        , flanker_7_id=request.json['flanker_7_id']
        , number_8_id=request.json['number_8_id']
        , scrum_half_id=request.json['scrum_half_id']
        , fly_half_id=request.json['fly_half_id']
        , wing_11_id=request.json['wing_11_id']
        , inside_centre_id=request.json['inside_centre_id']
        , outside_centre_id=request.json['outside_centre_id']
        , wing_14_id=request.json['wing_14_id']
        , full_back_id=request.json['full_back_id']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/squads/<int:id>', methods=['PUT'])
def update_squad(id):
    entity = squad.Squad.query.get(id)
    if not entity:
        abort(404)
    entity = squad.Squad(
        tighthead_id=request.json['tighthead_id'],
        loosehead_id=request.json['loosehead_id'],
        hooker_id=request.json['hooker_id'],
        lock_4_id=request.json['lock_4_id'],
        lock_5_id=request.json['lock_5_id'],
        flanker_6_id=request.json['flanker_6_id'],
        flanker_7_id=request.json['flanker_7_id'],
        number_8_id=request.json['number_8_id'],
        scrum_half_id=request.json['scrum_half_id'],
        fly_half_id=request.json['fly_half_id'],
        wing_11_id=request.json['wing_11_id'],
        inside_centre_id=request.json['inside_centre_id'],
        outside_centre_id=request.json['outside_centre_id'],
        wing_14_id=request.json['wing_14_id'],
        full_back_id=request.json['full_back_id'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/squads/<int:id>', methods=['DELETE'])
def delete_squad(id):
    entity = squad.Squad.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
