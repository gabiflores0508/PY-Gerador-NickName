import random

# Lista de adjetivos
ADJETIVOS = [
    "Rápido",
    "Sombrio",
    "Brilhante",
    "Feroz",
    "Misterioso",
    "Valente",
    "Implacável",
    "Ágil",
    "Silencioso",
    "Letal",
    "Invencível",
    "Estrategista",
    "Poderoso",
    "Mágico",
    "Furtivo",
    "Audacioso",
    "Corajoso",
    "Astuto",
    "Carismático",
    "Determinado",
    "Elétrico",
    "Explosivo",
    "Flamejante",
    "Gélido",
    "Luminoso",
    "Trevoso",
    "Sanguinário",
    "Inabalável",
    "Veloz",
    "Radiante",
    "Sábio",
    "Voraz",
    "Perigoso",
    "Tático",
    "Impetuoso",
    "Indomável",
    "Tenebroso",
    "Reluzente",
    "Enigmático",
    "Fantástico",
    "Eterno",
    "Fatal",
    "Vingador",
    "Protetor",
    "Glorioso",
    "Espetacular",
    "Celestial",
    "Cruel",
    "Brutal",
    "Ávido",
    "Ardente",
    "Rebelde",
    "Supremo",
    "Estelar",
    "Noturno",
    "Feroz",
    "Ártico",
    "Leal",
    "Destemido",
    "Renegado",
    "Ancestral",
    "Exímio",
    "Visionário",
    "Primordial",
]

# Lista de substantivos organizados por tema
SUBSTANTIVOS = {
    "fantasia": [
        "Dragão",
        "Mago",
        "Elfo",
        "Fada",
        "Cavaleiro",
        "Feiticeiro",
        "Bárbaro",
        "Oráculo",
        "Anjo",
        "Demônio",
        "Lobo",
        "Fênix",
        "Sereia",
        "Vampiro",
        "Licantropo",
        "Troll",
        "Gigante",
        "Espadachim",
        "Caçador",
        "Necromante",
        "Guardião",
        "Arqueiro",
        "Invocador",
        "Quimera",
        "Golem",
        "Elemental",
        "Ladino",
        "Sentinela",
        "Assassino",
        "Sombra",
    ],
    "tecnologia": [
        "Hacker",
        "Cyborg",
        "Glitch",
        "Bot",
        "Chip",
        "Código",
        "Firewall",
        "Drone",
        "Byte",
        "Núcleo",
        "Matrix",
        "Pixel",
        "Rede",
        "Criptógrafo",
        "AI",
        "Vírus",
        "Kernel",
        "Processador",
        "Servidor",
        "Banco",
        "Ether",
        "Chipset",
        "Quantum",
        "Frame",
        "Neural",
        "Robô",
        "Engrenagem",
        "Scanner",
        "Datalink",
        "Cipher",
    ],
    "espacial": [
        "Astro",
        "Galaxy",
        "Cometa",
        "Vortex",
        "Nebula",
        "Estrela",
        "Cosmo",
        "Planeta",
        "Meteorito",
        "Satélite",
        "Orbita",
        "Fóton",
        "Eclipse",
        "BuracoNegro",
        "Constelação",
        "Supernova",
        "Asteroide",
        "Quasar",
        "Pulsar",
        "Estação",
        "Explorador",
        "Astronauta",
        "Nave",
        "Propulsor",
        "Colônia",
        "Cratera",
        "Hiperespaço",
        "Viagem",
        "Gravidade",
        "Galáxia",
    ],
}

# Lista de símbolos
SIMBOLOS = ["*", "-", "_", "~", "!", "@", "#", "$", "%", "&"]
