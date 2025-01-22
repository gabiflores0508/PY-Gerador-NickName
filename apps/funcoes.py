import random
from apps.listas import ADJETIVOS, SUBSTANTIVOS, SIMBOLOS


def gerar_nickname_aleatorio(adjetivo, substantivo, simbolo="", numero=None):
    partes = [adjetivo, substantivo, simbolo]
    if numero is not None:
        partes.append(str(numero))
    random.shuffle(partes)
    return "".join(partes).strip()


def gerar_nickname_basico():
    adjetivo = random.choice(ADJETIVOS)
    tema = random.choice(list(SUBSTANTIVOS.keys()))
    substantivo = random.choice(SUBSTANTIVOS[tema])
    simbolo = random.choice(SIMBOLOS)
    numero = random.randint(10, 999)
    return gerar_nickname_aleatorio(adjetivo, substantivo, simbolo, numero)


def gerar_nickname_por_tema(tema=""):
    if tema not in SUBSTANTIVOS:
        tema = random.choice(list(SUBSTANTIVOS.keys()))
    adjetivo = random.choice(ADJETIVOS)
    substantivo = random.choice(SUBSTANTIVOS[tema])
    simbolo = random.choice(SIMBOLOS)
    numero = random.randint(10, 99)
    return gerar_nickname_aleatorio(adjetivo, substantivo, simbolo, numero)


def gerar_nickname_personalizado(
    tema="", incluir_simbolos=True, numero_customizado=None, inicial=""
):
    if tema not in SUBSTANTIVOS:
        tema = random.choice(list(SUBSTANTIVOS.keys()))
    adjetivo = random.choice(ADJETIVOS)
    substantivo = random.choice(SUBSTANTIVOS[tema])
    if inicial:
        substantivo = (
            inicial + substantivo
        )  # Adiciona a inicial no início do substantivo
    simbolo = random.choice(SIMBOLOS) if incluir_simbolos else ""
    numero = numero_customizado if numero_customizado else random.randint(10, 99)

    # Constrói o nickname com a inicial sempre no início
    partes = [substantivo, adjetivo, simbolo]
    if numero is not None:
        partes.append(str(numero))
    random.shuffle(partes[1:])  # Embaralha apenas os outros elementos
    return "".join(partes).strip()


def gerar_nickname_com_palavra_especifica(
    palavra, incluir_simbolos=True, numero_customizado=None
):
    adjetivo = random.choice(ADJETIVOS)
    simbolo = random.choice(SIMBOLOS) if incluir_simbolos else ""
    numero = numero_customizado if numero_customizado else random.randint(10, 99)

    # Constrói o nickname com a palavra no início
    partes = [palavra, adjetivo, simbolo]
    if numero is not None:
        partes.append(str(numero))
    random.shuffle(partes[1:])  # Embaralha apenas os outros elementos
    return "".join(partes).strip()
