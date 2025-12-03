import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

MODEL_PATH = "model.pkl"

def train_model(training_data_path):
    """
    Trains a Random Forest model to predict clicks.
    
    Args:
        training_data_path (str): Path to training CSV.
        
    Returns:
        model: Trained scikit-learn pipeline.
    """
    print(f"Training model using data from {training_data_path}...")
    df = pd.read_csv(training_data_path)
    
    X = df[['impressions', 'cost', 'device', 'country']]
    y = df['clicks']
    
    # Preprocessing for categorical data
    categorical_features = ['device', 'country']
    numerical_features = ['impressions', 'cost']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])
    
    # Pipeline
    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])
    
    model.fit(X, y)
    print("Model training completed.")
    return model

def save_model(model, path=MODEL_PATH):
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {path}")

def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return pickle.load(f)

def predict_performance(model, input_df):
    """
    Predicts clicks and CTR for the input dataframe.
    
    Args:
        model: Trained model.
        input_df (pd.DataFrame): Dataframe to predict on.
        
    Returns:
        pd.DataFrame: Dataframe with predictions.
    """
    print("Running predictions...")
    # Ensure input has necessary columns
    required_cols = ['impressions', 'cost', 'device', 'country']
    for col in required_cols:
        if col not in input_df.columns:
            # Add dummy if missing (for robustness, though input should have it)
            if col == 'device': input_df[col] = 'Unknown'
            elif col == 'country': input_df[col] = 'Unknown'
            else: input_df[col] = 0
            
    X_pred = input_df[required_cols]
    predicted_clicks = model.predict(X_pred)
    
    input_df['predicted_clicks'] = predicted_clicks
    input_df['predicted_ctr'] = (input_df['predicted_clicks'] / input_df['impressions']) * 100
    
    return input_df
