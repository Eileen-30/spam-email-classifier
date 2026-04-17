from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['email']
    
    # simple logic for now
    if "free" in data.lower():
        result = "Spam"
    else:
        result = "Not Spam"
    
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
