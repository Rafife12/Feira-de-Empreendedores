import FreeSimpleGUI as sg
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("projav3-16d41-firebase-adminsdk-fbsvc-b6c6255875.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

cadastro = ("nomeautor","nome", "categoria", "descricao", "local")
dados = {}

estados_siglas = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]
categorias=["Moda", "Saúde", "Beleza", "Esporte", "Tecnologia", "Gastronomia", "Educação","Entretenimento", "Artes"]

layout = [
    [sg.Text("Nome do negócio:"), sg.Input(key="nome")],
    [sg.Text("Nome do autor(a):"), sg.Input(key="nomeautor")],
    [sg.Text("Categoria:"), sg.Combo(categorias, key="categoria", readonly=True)],
    [sg.Text("Local (UF):"), sg.Combo(estados_siglas, key="local", readonly=True)],
    [sg.Text("Descrição:"), sg.Multiline(key="descricao", size=(30, 4))],
    [sg.Button("Cadastrar"), sg.Button("Sair")],
    [sg.Text("", key="mensagem", size=(40, 2))]
]

janela = sg.Window("Cadastrar empreendedor", layout)

while True:
    acao, valores = janela.read()

    if acao in (sg.WINDOW_CLOSED, "Sair"):
        break

    if acao == "Cadastrar":
        dados = {
            "nome": valores["nome"],
            "nomeautor": valores["nomeautor"],
            "categoria": valores["categoria"],
            "local": valores["local"],
            "descricao": valores["descricao"],
        }
        break

janela.close()

URL_IMAGEM_PADRAO = "https://grandesnomesdapropaganda.com.br/wp-content/uploads/2018/04/Qualy-campanha.jpg"
dados["imagem"] = URL_IMAGEM_PADRAO

db.collection("empreendedores").add(dados)
print("Cadastrado com sucesso!\n")

empreendedores_ref = db.collection("empreendedores")
docs = empreendedores_ref.stream()

for doc in docs:
    print(f"Id do empreendedor: {doc.id}\nInformações: {doc.to_dict()}\n")