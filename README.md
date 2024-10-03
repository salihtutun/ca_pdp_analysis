
# Context-Aware Partial Dependence Plot (CA-PDP) Analysis

## Overview
This Python package provides tools to perform Context-Aware Partial Dependence Plot (CA-PDP) analysis on any dataset. It includes functionality to handle clustering, model training, and PDP visualization in a modular structure.

## Key Features
- Modular Structure: Separated into classes for better readability and reusability.
- Supports Any Dataset: Automatically handles numerical and categorical data.
- Context-Aware Analysis: Uses clustering to segment data and perform context-specific analyses.
- Visualization: Creates both global and cluster-specific Partial Dependence Plots.

## Installation
To install the package from PyPI, use:

```bash
pip install ca-pdp-analysis
```

## Usage
Here is a sample usage of the package:

```python
from ca_pdp_analysis import DataProcessor, ModelTrainer, PDPAnalyzer
from sklearn.cluster import KMeans

# Load and preprocess the dataset
processor = DataProcessor(file_path="adult.csv", target_column="income")
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
```

## Requirements
- Python 3.6 or later
- numpy
- pandas
- scikit-learn
- matplotlib
- scipy

## License
MIT License
