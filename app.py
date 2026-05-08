from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import predict_survival

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features
        prediction, probability = predict_survival(
            pclass=int(data['Pclass']),
            sex=data['Sex'],
            age=float(data['Age']),
            sibsp=int(data['SibSp']),
            parch=int(data['Parch']),
            fare=float(data['Fare']),
            embarked=data['Embarked']
        )
        
        return jsonify({
            'prediction': prediction,
            'probability': probability,
            'result': 'Survived' if prediction == 1 else 'Did not survive'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)