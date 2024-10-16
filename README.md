
# CA PDP Analysis

## Project Overview
This repository contains an implementation of a **Partial Dependence Plot (PDP) Analysis** tool designed to assist in feature interpretation for machine learning models. The project includes scripts for data preprocessing, model training, and visualizing the interactions between features and model predictions.

### Main Features
- **Data Processing**: Clean and transform raw data into a suitable format for model training.
- **Model Training**: Train machine learning models using user-defined configurations.
- **Partial Dependence Plot (PDP) Analysis**: Generate PDPs to visualize and understand how feature values influence model predictions.
- **Feature Interactions**: Examine feature dependencies and interactions for enhanced model interpretability.

### Directory Structure
The directory structure of the project is as follows:

```
ca_pdp_analysis/
│
├── README.md                # Project documentation (this file)
├── requirements.txt         # Python dependencies required for the project
├── setup.py                 # Setup script for the project
├── test.py                  # Unit tests for project modules
├── adult.csv                # Example dataset for demonstration
│
├── ca_pdp_analysis/         # Main project directory
│   ├── __init__.py          # Package initialization file
│   ├── data_processor.py    # Module for data processing
│   ├── model_trainer.py     # Module for training machine learning models
│   ├── pdp_analyzer.py      # Main module for PDP analysis
│
└── build/                   # Build directory for packaging the module
```

### Requirements
Before running the scripts, ensure that you have all the necessary Python packages installed. The `requirements.txt` file lists all dependencies. Install them using the following command:

```bash
pip install -r requirements.txt
```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/salihtutun/ca_pdp_analysis.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd ca_pdp_analysis
   ```

3. Install the package:
   ```bash
   python setup.py install
   ```

### Getting Started
#### 1. Data Preparation
The first step is to preprocess the data using the `data_processor.py` script. This module will clean, normalize, and prepare the dataset for model training and analysis.

Example usage:

```python
from ca_pdp_analysis.data_processor import DataProcessor

# Load and preprocess the data
processor = DataProcessor("path_to_dataset.csv")
processed_data = processor.process()
```

#### 2. Model Training
Once the data is prepared, use the `model_trainer.py` script to train a machine learning model. By default, it supports models such as Random Forest, XGBoost, and Decision Trees. You can extend it to support more models as needed.

Example usage:

```python
from ca_pdp_analysis.model_trainer import ModelTrainer

# Initialize and train a model
trainer = ModelTrainer(data=processed_data, target_column="target")
model = trainer.train_model(model_type="random_forest")
```

#### 3. PDP Analysis
To analyze and visualize feature impacts using Partial Dependence Plots, utilize the `pdp_analyzer.py` script. This script generates plots to help understand the influence of each feature.

Example usage:

```python
from ca_pdp_analysis.pdp_analyzer import PDPAnalyzer

# Create a PDP analyzer instance
analyzer = PDPAnalyzer(model, data=processed_data, target_column="target")

# Generate PDP plots for a specific feature
analyzer.plot_pdp(feature="feature_name")
```

### Example Usage
The `adult.csv` dataset provided in the repository can be used to quickly test the functionality of the scripts. Here’s how to run the entire pipeline:

1. **Data Processing**:
   ```python
   from ca_pdp_analysis.data_processor import DataProcessor
   processor = DataProcessor("adult.csv")
   processed_data = processor.process()
   ```

2. **Model Training**:
   ```python
   from ca_pdp_analysis.model_trainer import ModelTrainer
   trainer = ModelTrainer(data=processed_data, target_column="income")
   model = trainer.train_model(model_type="xgboost")
   ```

3. **PDP Analysis**:
   ```python
   from ca_pdp_analysis.pdp_analyzer import PDPAnalyzer
   analyzer = PDPAnalyzer(model, data=processed_data, target_column="income")
   analyzer.plot_pdp(feature="age")
   ```

### Available Scripts
- **`data_processor.py`**: Handles data preprocessing tasks such as cleaning, normalization, and encoding.
- **`model_trainer.py`**: Trains various machine learning models based on user configuration.
- **`pdp_analyzer.py`**: Generates Partial Dependence Plots to understand feature impacts.

### Extending the Project
To add new features or models:
1. **Data Processing**: Extend `data_processor.py` to include new transformation techniques.
2. **Model Training**: Add new algorithms to `model_trainer.py`.
3. **PDP Analysis**: Enhance `pdp_analyzer.py` to support new visualizations and interpretations.

### Troubleshooting & Common Issues
1. **Installation Errors**: Ensure that `pip` is updated and all required libraries are installed.
   ```bash
   pip install --upgrade pip
   ```

2. **Model Not Training Properly**: Check the target column and ensure it matches the correct label in your dataset.

3. **Plots Not Showing**: Make sure you have `matplotlib` and `seaborn` installed.

### Contributing
We welcome contributions to the project! Please follow these steps to submit your contributions:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contact
For any inquiries or support, please contact:
- **Name**: Salih Tutun
- **Email**: [salihtutun@wustl.edu](mailto:salihtutun@wustl.edu)
- **GitHub**: [Salih Tutun](https://github.com/salihtutun)
