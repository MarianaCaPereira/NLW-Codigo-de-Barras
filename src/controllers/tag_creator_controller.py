from typing import Dict
from src.drivers.barcode_handle import BarcodeHandler

class TagCreatorController:
    '''
    Responsabilidade de implementar a regra de negócio
    '''
    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response

    # Dois __ quer dizer que é um metódo privado da classe
    def __create_tag(self, product_code: str) -> str:  # Criar a tag
        barcode_handle = BarcodeHandler()
        path_from_tag = barcode_handle.create_barcode(product_code)
        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        # Formatar a resposta para ser devolvida
        return{
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
