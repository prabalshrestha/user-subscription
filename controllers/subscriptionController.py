from flask import Blueprint,request,jsonify,make_response
from services.subscriptionPlanService import SubscriptionPlanService
import json


subscription_plan_blueprint=Blueprint('plans',__name__,url_prefix='/plans')
service=SubscriptionPlanService()

@subscription_plan_blueprint.route('/',methods=['GET'])
def get_plans():
    plans=service.get_subscription_plans()
    if plans:
        return make_response(jsonify({'plans':plans}),200)