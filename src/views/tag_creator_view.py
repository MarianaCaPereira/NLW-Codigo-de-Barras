from src.views.http_types.http_request import HttpResquest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    Responsabilidade para interagir com o HTTP
    '''
    # Métodos em classe tem o self
    # Lógica de regra de negócio
    # retorno http
    def validate_and_create(self, http_request: HttpResquest) -> HttpResponse:
        #body = http_request.body
        #product_code = body["product_code"]

        print('estou na minha view')
        print(http_request)
        return HttpResponse(status_code=200, body={"hello": "world"})
