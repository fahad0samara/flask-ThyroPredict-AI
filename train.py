import pandas as pd
from src.models.trainer import ThyroidModelTrainer
from src.config import Config
import os

def main():
    """Main function to train and save the model."""
    try:
        # Create data directory if it doesn't exist
        os.makedirs(Config.DATA_DIR, exist_ok=True)
        
        # Load data
        data_file = os.path.join(Config.DATA_DIR, 'thyroid_cancer_risk_data.csv')
        data = pd.read_csv(data_file)
        
        print("Loading and preparing data...")
        
        # Initialize trainer
        trainer = ThyroidModelTrainer()
        
        # Train model
        print("Training model...")
        metrics = trainer.train(data)
        
        # Save model and preprocessing objects
        print("Saving model and preprocessing objects...")
        trainer.save_models()
        
        # Print metrics
        print("\nTraining Results:")
        print(f"Accuracy: {metrics['accuracy']:.4f}")
        print("\nClassification Report:")
        print(metrics['classification_report'])
        
        print("\nModel and preprocessing objects saved successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
