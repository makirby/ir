from app import app, db
from app.models import player
from flask import abort, jsonify, request
import datetime
import json


@app.route('/inforugby/players', methods=['GET'])
def get_all_players():
    entities = player.Player.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/inforugby/players/<int:id>', methods=['GET'])
def get_player(id):
    entity = player.Player.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/inforugby/players', methods=['POST'])
def create_player():
    entity = player.Player(
        name=request.json['name']
        , date_of_birth=datetime.datetime.strptime(request.json['date_of_birth'], "%Y-%m-%d").date()
        , height=request.json['height']
        , weight=request.json['weight']
        , player_text=request.json['player_text']
        , retired=request.json['retired']
        , user_created=request.json['user_created']
        , image_location=request.json['image_location']
        , icon_location=request.json['icon_location']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


@app.route('/inforugby/players/<int:id>', methods=['PUT'])
def update_player(id):
    entity = player.Player.query.get(id)
    if not entity:
        abort(404)
    entity = player.Player(
        name=request.json['name'],
        date_of_birth=datetime.datetime.strptime(request.json['date_of_birth'], "%Y-%m-%d").date(),
        height=request.json['height'],
        weight=request.json['weight'],
        player_text=request.json['player_text'],
        retired=request.json['retired'],
        user_created=request.json['user_created'],
        image_location=request.json['image_location'],
        icon_location=request.json['icon_location'],
        id=id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200


@app.route('/inforugby/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    entity = player.Player.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
