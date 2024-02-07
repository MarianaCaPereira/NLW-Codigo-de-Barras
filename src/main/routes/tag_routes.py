from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpResquest
from src.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"]) # Rota

def create_tags():
    tag_creator_view = TagCreatorView() # View

    http_request = HttpResquest(body=request.json) # HTTP
    response = tag_creator_view.validate_and_create(http_request) #HTTP na view

    return jsonify(response.body), response.status_code #Retornar informação
