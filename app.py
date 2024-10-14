from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["ualabi_db"]
collection = db["ualabis"]


@app.route("/ualabis", methods=["POST"])
def crear_ualabi():
    data = request.get_json()
    nombre = data.get("nombre")
    edad = data.get("edad")
    peso = data.get("peso")

    if not nombre or not edad or not peso:
        return jsonify({"error": "Faltan datos necesarios"}), 400

    nuevo_ualabi = {"nombre": nombre, "edad": edad, "peso": peso}

    result = collection.insert_one(nuevo_ualabi)
    return jsonify({"message": "Ualabi creado", "id": str(result.inserted_id)}), 201


@app.route("/ualabis", methods=["GET"])
def leer_ualabis():
    ualabis = list(collection.find())
    resultado = []

    for ualabi in ualabis:
        resultado.append(
            {
                "id": str(ualabi["_id"]),
                "nombre": ualabi["nombre"],
                "edad": ualabi["edad"],
                "peso": ualabi["peso"],
            }
        )

    return jsonify(resultado), 200


@app.route("/ualabis/<id>", methods=["GET"])
def leer_ualabi(id):
    ualabi = collection.find_one({"_id": ObjectId(id)})

    if ualabi:
        return (
            jsonify(
                {
                    "id": str(ualabi["_id"]),
                    "nombre": ualabi["nombre"],
                    "edad": ualabi["edad"],
                    "peso": ualabi["peso"],
                }
            ),
            200,
        )
    else:
        return jsonify({"error": "Ualabi no encontrado"}), 404


@app.route("/ualabis/<id>", methods=["PUT"])
def actualizar_ualabi(id):
    data = request.get_json()
    nombre = data.get("nombre")
    edad = data.get("edad")
    peso = data.get("peso")

    if not nombre or not edad or not peso:
        return jsonify({"error": "Faltan datos necesarios"}), 400

    resultado = collection.update_one(
        {"_id": ObjectId(id)}, {"$set": {"nombre": nombre, "edad": edad, "peso": peso}}
    )

    if resultado.matched_count == 1:
        return jsonify({"message": "Ualabi actualizado"}), 200
    else:
        return jsonify({"error": "Ualabi no encontrado"}), 404


@app.route("/ualabis/<id>", methods=["DELETE"])
def eliminar_ualabi(id):
    resultado = collection.delete_one({"_id": ObjectId(id)})

    if resultado.deleted_count == 1:
        return jsonify({"message": "Ualabi eliminado"}), 200
    else:
        return jsonify({"error": "Ualabi no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
