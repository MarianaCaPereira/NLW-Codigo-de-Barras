from src.views.http_types.http_response import HttpResponse

#Erro como obj, erro = execeção
def handle_errors(error: Exception) -> HttpResponse:
    # Trator o erro de forma genérica
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
