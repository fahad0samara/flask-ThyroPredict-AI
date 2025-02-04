import os

class Config:
    # Application settings
    APP_NAME = "ThyroPredict AI - Advanced Thyroid Cancer Risk Assessment"
    DEBUG = True
    PORT = 1231
    HOST = '0.0.0.0'

    # Path configurations
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    MODEL_DIR = os.path.join(BASE_DIR, 'models')
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

    # Model files
    MODEL_FILE = os.path.join(MODEL_DIR, 'best_model.joblib')
    SCALER_FILE = os.path.join(MODEL_DIR, 'scaler.joblib')
    LABEL_ENCODERS_FILE = os.path.join(MODEL_DIR, 'label_encoders.joblib')
    TARGET_ENCODER_FILE = os.path.join(MODEL_DIR, 'target_encoder.joblib')

    # Feature configurations
    CATEGORICAL_VARS = [
        'Gender', 'Country', 'Ethnicity', 'Family_History',
        'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking',
        'Obesity', 'Diabetes'
    ]
    
    NUMERICAL_VARS = [
        'Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size'
    ]

    # Valid values for categorical variables
    VALID_VALUES = {
        'Gender': ['Male', 'Female'],
        'Country': ['USA', 'UK', 'China', 'India', 'Japan', 'Germany', 
                   'Brazil', 'Russia', 'South Korea', 'Nigeria'],
        'Ethnicity': ['African', 'Asian', 'Caucasian', 'Hispanic', 'Middle Eastern'],
        'Binary_Fields': ['Yes', 'No']  # For all yes/no fields
    }

    # Risk score weights
    RISK_WEIGHTS = {
        'Family_History': 2.0,
        'Radiation_Exposure': 1.5,
        'Iodine_Deficiency': 1.5,
        'Smoking': 1.0,
        'Obesity': 1.0,
        'Diabetes': 1.0
    }
