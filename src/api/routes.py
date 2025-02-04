from flask import request, jsonify, render_template
from . import app
from ..models.predictor import ThyroidPredictor
import pandas as pd

# Initialize predictor
predictor = ThyroidPredictor()

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/batch')
def batch():
    """Render the batch prediction page."""
    return render_template('batch.html')

@app.route('/api-docs')
def api_docs():
    """Render the API documentation page."""
    return render_template('api_docs.html')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    status = {
        'status': 'healthy' if predictor.model is not None else 'unhealthy',
        'model_loaded': predictor.model is not None,
        'scaler_loaded': predictor.scaler is not None,
        'label_encoders_loaded': predictor.label_encoders is not None,
        'target_encoder_loaded': predictor.target_encoder is not None
    }
    return jsonify(status)

@app.route('/predict', methods=['POST'])
def predict():
    """Single prediction endpoint."""
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Make prediction
        result = predictor.predict(data)
        return jsonify(result)

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """Batch prediction endpoint."""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read CSV file
        df = pd.read_csv(file)
        
        # Make predictions for each row
        results = []
        for _, row in df.iterrows():
            try:
                result = predictor.predict(row.to_dict())
                results.append(result)
            except Exception as e:
                results.append({'error': str(e)})
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
