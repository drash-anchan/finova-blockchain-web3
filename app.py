from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(bk)
blockchain = Blockchain()
@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    data = request.get_json()

    required_fields = ["sender", "receiver", "amount"]
    if not all(field in data for field in required_fields):
        return "Missing fields", 400

    blockchain.add_transaction(
        data["sender"],
        data["receiver"],
        data["amount"]
    )

    return jsonify({"message": "Transaction added"}), 201

@app.route("/mine", methods=["GET"])
def mine():
    blockchain.mine_pending_transactions()
    return jsonify({"message": "Block mined"}), 200

@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": block.transactions,
            "hash": block.hash,
            "previous_hash": block.previous_hash
        })
    return jsonify(chain_data), 200

@app.route("/validate", methods=["GET"])
def validate():
    is_valid = blockchain.is_chain_valid()
    return jsonify({"valid": is_valid}), 200

if bk == "__main__":
    app.run(port=5000)
