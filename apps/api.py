from flask import Blueprint, request, jsonify
from apps.funcoes import gerar_nickname_personalizado

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/gerar_nickname", methods=["POST"])
def gerar_nickname():
    data = request.json

    tipo = data.get("tipo")

    if tipo == "personalizado":
        tema = data.get("tema", "default")
        incluir_simbolos = data.get("incluir_simbolos", True)
        numero_customizado = data.get("numero_customizado")
        inicial = data.get("inicial", "")

        if not inicial.isalpha() or len(inicial) != 1:
            return jsonify({"error": "Inicial inválida"}), 400

        nickname = gerar_nickname_personalizado(
            tema, incluir_simbolos, numero_customizado, inicial
        )

    else:
        return jsonify({"error": "Tipo de nickname inválido"}), 400

    return jsonify({"nickname": nickname})
