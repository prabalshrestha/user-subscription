from flask import Blueprint,request,jsonify,make_response
from services.userService import UserService
import json

user_blueprint=Blueprint('task',__name__)
service=UserService()

@user_blueprint.route('/user',methods=['POST'])
def add_user():
    user=request.get_json()
    user = service.add_user(user)
    return make_response(jsonify(user),201)

@user_blueprint.route('/user/<int:user_id>',methods=['GET'])
def get_user_by_id(user_id):
    user=service.get_user_by_id(user_id)
    if user:
        return make_response(jsonify({'user':user}),200)
    else:
        return make_response(jsonify({'ErrMsg':"User not found"}),404)

@user_blueprint.route('/users',methods=['GET'])
def get_all_users():
    user=service.get_all_users()
    if user:
        return make_response(jsonify({'users':user}),200)
    else:
        return make_response(jsonify({'ErrMsg':"User not found"}),404)

@user_blueprint.route('/user/<int:user_id>/subscribe',methods=['PUT'])
def subscribe(user_id):
    request_data = request.get_json()
    plan=request_data['plan']
    try:
        ur_plan = service.subscribe(user_id,plan)
        return make_response(jsonify({"plan":ur_plan}),201)
    except Exception as e:
        return make_response(jsonify({"error":"Invaild plan"}),400)
