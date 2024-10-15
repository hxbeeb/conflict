from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the AI-Powered Conflict Resolution Mediator!")

@app.route('/api/resolve', methods=['POST'])
def resolve_conflict():
    data = request.get_json()
    
    # Input validation
    if not data or 'party1' not in data or 'party2' not in data:
        return jsonify(error="Missing data"), 400  # Return 400 for missing data

    # Sample conflict resolution logic (for demonstration)
    response = {
        "resolved_conflict": {
            "party1": data['party1'],
            "party2": data['party2']
        },
        "success": True
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
