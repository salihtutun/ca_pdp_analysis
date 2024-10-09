from ca_pdp_analysis import DataProcessor, ModelTrainer, PDPAnalyzer
from sklearn.cluster import KMeans

# Load and preprocess the dataset using ' <=50K' as the new target column
processor = DataProcessor(file_path="adult.csv", target_column=" <=50K")
X, y = processor.load_and_preprocess_data()

# Create clusters
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# Train a Gradient Boosting model
trainer = ModelTrainer(X, y)
model = trainer.train_gradient_boosting()

# Calculate and plot PDPs for a feature (e.g., 'age')
pdp_analyzer = PDPAnalyzer(model, X, clusters, feature_idx=0)
local_pdps = pdp_analyzer.calculate_local_pdps()
pdp_analyzer.plot_pdp(local_pdps, feature_name="age")
