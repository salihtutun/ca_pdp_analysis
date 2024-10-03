
import pandas as pd

class DataProcessor:
    def __init__(self, file_path: str, target_column: str):
        self.file_path = file_path
        self.target_column = target_column

    def load_and_preprocess_data(self) -> tuple:
        """Load and preprocess the dataset."""
        data = pd.read_csv(self.file_path)
        data_cleaned = data.dropna()
        X = data_cleaned.drop(columns=[self.target_column])
        y = data_cleaned[self.target_column]
        
        # Convert categorical features to numerical
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()
        if categorical_features:
            X_encoded = pd.get_dummies(X, columns=categorical_features, drop_first=True)
        else:
            X_encoded = X.copy()
        return X_encoded, y
