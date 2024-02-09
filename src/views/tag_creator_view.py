from src.views.http_types.http_request import HttpResquest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
    Responsabilidade para interagir com o HTTP
    '''
    # Métodos em classe tem o self
    # Lógica de regra de negócio
    # retorno http
    def validate_and_create(self, http_request: HttpResquest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()
        body = http_request.body
        product_code = body["product_code"]

        # Lógica de regra de negócio
        formatted_response = tag_creator_controller.create(product_code)

        # retorno http
        return HttpResponse(status_code=200, body=formatted_response) # Entregar para o usuário
