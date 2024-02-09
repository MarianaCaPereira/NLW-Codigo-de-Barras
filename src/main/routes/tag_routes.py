from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpResquest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"]) # Rota

def create_tags():
    response = None
    try:
        tag_creator_view = TagCreatorView() # View

        http_request = HttpResquest(body=request.json) # HTTP
        response = tag_creator_view.validate_and_create(http_request) #HTTP na view
    except Exception as exception:
        response = handle_errors(exception) # Resposta em formato Http

    return jsonify(response.body), response.status_code #Retornar informação
