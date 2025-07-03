from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS

cred = credentials.Certificate("projav3-16d41-firebase-adminsdk-fbsvc-b073edb1ff.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
CORS(app)

@app.route("/empreendedores", methods=["GET"])
def listar_empreendedores():
    empreendedores_ref = db.collection("empreendedores")
    docs = empreendedores_ref.stream()

    lista = []
    for doc in docs:
        dados = doc.to_dict()
        dados["id"] = doc.id  # opcional: inclui o ID do documento
        lista.append(dados)

    return jsonify(lista)

if __name__ == "__main__":

    app.run(debug=True)