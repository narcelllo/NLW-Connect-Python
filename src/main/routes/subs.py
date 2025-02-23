from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.controllers.subscribers.subscriber_creator_controller import SubscriberCreatorController
from src.model.repositories.subsctribers_repository import SubscribersRepository

subs_route_bp = Blueprint("subs_route", __name__)

@subs_route_bp.route("/subscribers", methods=["POST"])
def create_new_subs():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subs_repo = SubscribersRepository()
    subs_creator = SubscriberCreatorController(subs_repo)

    http_response = subs_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code