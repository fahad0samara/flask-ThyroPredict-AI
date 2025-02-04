# ThyroPredict AI - Advanced Thyroid Cancer Risk  

An advanced machine learning-powered API for early thyroid cancer risk assessment, featuring a modern glassmorphism UI and comprehensive analysis tools.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green)
![XGBoost](https://img.shields.io/badge/XGBoost-1.4.2-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

##  Key Features

###  Clinical Assessment
- **Advanced Risk Prediction**: Uses XGBoost model for accurate cancer risk assessment
- **Multi-factor Analysis**: Considers 14+ risk factors including:
  - Hormone Levels (TSH, T3, T4)
  - Nodule Characteristics
  - Patient Demographics
  - Medical History
- **Risk Score Calculation**: Weighted analysis of critical risk factors

###  Modern Interface
- **Glassmorphism Design**: Beautiful, modern UI with:
  - Frosted glass effects
  - Smooth animations
  - Responsive layout
- **Interactive Forms**: Real-time validation and feedback
- **Mobile-Friendly**: Fully responsive design for all devices

###  Multiple Prediction Methods
- **Single Patient Assessment**: Individual risk evaluation
- **Batch Processing**: Analyze multiple patients via CSV upload
- **RESTful API**: Programmatic access for integration

###  Advanced Features
- **Comprehensive Reporting**: Detailed risk analysis and recommendations
- **Data Validation**: Robust input validation and error handling
- **Health Monitoring**: System health and model status checks

##  Project Structure

```
thyroid-cancer-analysis/
├── data/                      # Data directory
│   └── thyroid_cancer_risk_data.csv
├── models/                    # Model files
│   ├── best_model.joblib     # Trained XGBoost model
│   ├── scaler.joblib         # Feature scaler
│   ├── label_encoders.joblib # Categorical encoders
│   └── target_encoder.joblib # Target variable encoder
├── src/                      # Source code
│   ├── api/                  # API implementation
│   ├── models/               # ML model logic
│   └── config.py            # Configuration
├── static/                   # Static assets
│   └── css/
├── templates/                # HTML templates
└── requirements.txt         # Dependencies
```

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/thyropredict-ai.git
   cd thyropredict-ai
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:
   ```bash
   python run.py
   ```

Visit http://localhost:1231 to access the application.

##  API Reference

### Health Check
```http
GET /health
```

### Single Prediction
```http
POST /predict
Content-Type: application/json

{
    "Age": 45,
    "Gender": "Female",
    "TSH_Level": 2.5,
    "T3_Level": 1.8,
    "T4_Level": 10.5,
    "Nodule_Size": 2.3,
    ...
}
```

### Batch Prediction
```http
POST /batch_predict
Content-Type: multipart/form-data
```

##  Model Performance

- **Accuracy**: 85%+ on validation set
- **Sensitivity**: 82% for high-risk cases
- **Specificity**: 88% for low-risk cases
- **AUC-ROC**: 0.89

##  Security Features

- Input validation and sanitization
- Error handling and logging
- Rate limiting for API endpoints
- Secure data processing

##  Development

### Technology Stack
- **Backend**: Flask, Python 3.8+
- **ML Framework**: XGBoost, Scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Glassmorphism UI, Bootstrap

### Best Practices
- Type hints for better code quality
- Comprehensive documentation
- Unit tests for critical components
- Clean code architecture

##  Future Enhancements

1. **AI/ML Improvements**
   - Deep learning integration
   - Real-time model updates
   - Additional biomarker support

2. **Feature Additions**
   - PDF report generation
   - Multi-language support
   - Advanced visualization

3. **Technical Updates**
   - Docker containerization
   - CI/CD pipeline
   - Cloud deployment options

##  Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- Medical research papers and guidelines
- Open-source ML community
- UI/UX design inspiration
- Contributors and testers

##  Contact

For questions and support, please open an issue or contact the maintainers.

---
Made with  for advancing medical diagnostics
