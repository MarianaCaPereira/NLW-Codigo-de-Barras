from flask import Flask, request, jsonify
from barcode import Code128 # Tipo de codificação
from barcode.writer import ImageWriter

app = Flask(__name__)  # Servidor em flask

# @ =  decorador
@app.route('/create_tag', methods=["POST"]) # Rota
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jsonify({"tag path": path_from_tag})

if __name__ =='__main__':  # main em python
    app.run(host='0.0.0.0', port=3000) # Criando servidor em flask
    # localhost na porta 3000
