from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/name_length', methods=['POST'])
def name_length():
    data = request.get_json()
    name = data.get('name', '')
    length = len(name)
    response = {'length': length}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
