
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

class ModelTrainer:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def train_gradient_boosting(self) -> GradientBoostingClassifier:
        """Train a Gradient Boosting Classifier."""
        model = GradientBoostingClassifier(n_estimators=100, random_state=42)
        X_train, _, y_train, _ = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        return model
