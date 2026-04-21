import pymongo
from datetime import datetime
from bson.objectid import ObjectId

# 1. Ligação ao Servidor
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["airbnb_clone"]

# Limpar as coleções para evitar duplicados ao testar
db.usuarios.delete_many({})
db.locais.delete_many({})
db.reservas.delete_many({})

# --- 2. MOCK DE UTILIZADORES (Anfitriões e Hóspedes) ---
usuarios_data = [
    {
        "_id": ObjectId("65df00000000000000000001"),
        "nome": "Carlos Oliveira",
        "email": "carlos@email.com",
        "tipo": "anfitriao",
        "data_cadastro": datetime(2024, 5, 10)
    },
    {
        "_id": ObjectId("65df00000000000000000002"),
        "nome": "Maria Souza",
        "email": "maria@email.com",
        "tipo": "hospede",
        "data_cadastro": datetime(2025, 2, 15)
    },
    {
        "_id": ObjectId("65df00000000000000000003"),
        "nome": "Ana Martins",
        "email": "ana@email.com",
        "tipo": "ambos",
        "data_cadastro": datetime(2026, 1, 20)
    }
]

# --- 3. MOCK DE LOCAIS (Propriedades) ---
locais_data = [
    {
        "_id": ObjectId("75ef00000000000000000001"),
        "anfitriao_id": ObjectId("65df00000000000000000001"), # Carlos
        "titulo": "Studio Moderno - Copacabana",
        "descricao": "A 2 minutos da praia com Wi-Fi de alta velocidade.",
        "preco_por_noite": 220.0,
        "endereco": {"cidade": "Rio de Janeiro", "estado": "RJ", "pais": "Brasil"},
        "comodidades": ["Wi-Fi", "Ar Condicionado", "Elevador"]
    },
    {
        "_id": ObjectId("75ef00000000000000000002"),
        "anfitriao_id": ObjectId("65df00000000000000000001"), # Carlos
        "titulo": "Casa de Campo com Lareira",
        "descricao": "Ideal para fins de semana relaxantes na serra.",
        "preco_por_noite": 450.0,
        "endereco": {"cidade": "Petrópolis", "estado": "RJ", "pais": "Brasil"},
        "comodidades": ["Piscina", "Lareira", "Churrasqueira"]
    },
    {
        "_id": ObjectId("75ef00000000000000000003"),
        "anfitriao_id": ObjectId("65df00000000000000000003"), # Ana
        "titulo": "Loft Minimalista - Vila Madalena",
        "descricao": "Perto de bares, galerias de arte e metro.",
        "preco_por_noite": 310.0,
        "endereco": {"cidade": "São Paulo", "estado": "SP", "pais": "Brasil"},
        "comodidades": ["Wi-Fi", "Academia", "Varanda"]
    }
]

# --- 4. MOCK DE RESERVAS (Controle de Aluguer) ---
reservas_data = [
    {
        "local_id": ObjectId("75ef00000000000000000001"), # Studio Copacabana
        "hospede_id": ObjectId("65df00000000000000000002"), # Maria
        "datas": {
            "checkin": datetime(2026, 6, 1, 14, 0),
            "checkout": datetime(2026, 6, 5, 11, 0)
        },
        "valor_total": 880.0, # 4 noites * 220
        "status": "confirmada",
        "data_reserva": datetime.now()
    },
    {
        "local_id": ObjectId("75ef00000000000000000003"), # Loft Vila Madalena
        "hospede_id": ObjectId("65df00000000000000000002"), # Maria
        "datas": {
            "checkin": datetime(2026, 7, 10, 14, 0),
            "checkout": datetime(2026, 7, 12, 11, 0)
        },
        "valor_total": 620.0,
        "status": "pendente",
        "data_reserva": datetime.now()
    }
]

# Inserção dos dados
db.usuarios.insert_many(usuarios_data)
db.locais.insert_many(locais_data)
db.reservas.insert_many(reservas_data)

print("Mock de dados inserido com sucesso!")