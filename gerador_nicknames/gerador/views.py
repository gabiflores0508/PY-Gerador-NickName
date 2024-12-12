from django.shortcuts import render
from .funcoes import (
    gerar_nickname_basico,
    gerar_nickname_por_tema,
    gerar_nickname_personalizado,
    gerar_nickname_com_palavra_especifica,
)


def index(request):
    return render(request, "index.html")


def gerar_nickname(request):
    opcao = request.POST.get("opcao")
    tema = request.POST.get("tema", "").strip().lower()
    inicial = request.POST.get("inicial", "").strip()
    palavra = request.POST.get("palavra", "").strip()
    incluir_simbolos = "simbolos" in request.POST
    numero_customizado = request.POST.get("numero", "").strip()

    # Converter número customizado para inteiro, se possível
    if numero_customizado.isdigit():
        numero_customizado = int(numero_customizado)
    else:
        numero_customizado = None

    if opcao == "basico":
        nickname = gerar_nickname_basico()
    elif opcao == "tema":
        nickname = gerar_nickname_por_tema(tema)
    elif opcao == "personalizado":
        nickname = gerar_nickname_personalizado(
            tema, incluir_simbolos, numero_customizado, inicial
        )
    elif opcao == "palavra":
        nickname = gerar_nickname_com_palavra_especifica(
            palavra, incluir_simbolos, numero_customizado
        )
    else:
        nickname = "Opção inválida"

    return render(request, "result.html", {"nickname": nickname})
