import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("projav3-16d41-firebase-adminsdk-fbsvc-b073edb1ff.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

cadastro = ("nome", "categoria", "descricao", "identidade", "local")
dados = {}

for campo in cadastro:
    dado = input(f"Digite '{campo}': ")
    dados[campo] = dado

URL_IMAGEM_PADRAO = "https://grandesnomesdapropaganda.com.br/wp-content/uploads/2018/04/Qualy-campanha.jpg"
dados["imagem"] = URL_IMAGEM_PADRAO

db.collection("empreendedores").add(dados)
print("Cadastrado com sucesso!\n")

empreendedores_ref = db.collection("empreendedores")
docs = empreendedores_ref.stream()

for doc in docs:
    print(f"Id do empreendedor: {doc.id}\nInformações: {doc.to_dict()}\n")