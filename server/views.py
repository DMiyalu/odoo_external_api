from flask import Flask, jsonify
from services.odoo import Partners

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return "Welcome on API"


@app.route('/api/partners/', methods=['GET'])
def get_all_partners():
    response = Partners.get_all_partners()
    if response is None: return jsonify({'status': '404'})
    return jsonify({'status': 200, 'data': response})


@app.route('/api/partners/<int:id>', methods=['GET'])
def get_partner_by_id(id):
    response = Partners.get_partner(id)
    # if response is None: return jsonify({'status': '404'})
    return jsonify({'status': 200, 'data': response})


@app.route('/api/partners/<int:id>', methods=['DELETE'])
def delete_partner(id):
    response = Partners.delete_partner(id)
    # if response.result.status_code == 2: return jsonify({'status': '500'})
    return jsonify({'status': 200, 'data': response})


@app.route('/api/partners/<int:id>', methods=['PUT'])
def update_partner(id):
    response = Partners.update_partner(id, "Dido")
    # if response.result.status_code == 2: return jsonify({'status': '500'})
    return jsonify({'status': 200, 'data': response})


@app.route('/api/partners/', methods=['POST'])
def create_partner():
    response = Partners.create_partner("Aspic")
    # if response.result.status_code == 2: return jsonify({'status': '500'})
    return jsonify({'status': 200, 'data': response})

if __name__ == "__main__":
    app.run()