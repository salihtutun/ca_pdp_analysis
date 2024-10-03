
import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import partial_dependence

class PDPAnalyzer:
    def __init__(self, model, X, clusters, feature_idx):
        self.model = model
        self.X = X
        self.clusters = clusters
        self.feature_idx = feature_idx

    def calculate_local_pdps(self):
        """Calculate PDP for each cluster."""
        local_pdps = {}
        for cluster in np.unique(self.clusters):
            cluster_indices = np.where(self.clusters == cluster)[0]
            pdp_values = partial_dependence(self.model, self.X.values[cluster_indices], [self.feature_idx])
            local_pdps[cluster] = pdp_values
        return local_pdps

    def plot_pdp(self, local_pdps, feature_name):
        """Plot the PDPs for each cluster."""
        plt.figure(figsize=(12, 8))
        colors = ['blue', 'orange', 'green']
        for idx, cluster in enumerate(local_pdps):
            plt.plot(local_pdps[cluster]['values'][0], local_pdps[cluster]['average'][0], color=colors[idx], label=f'Cluster {cluster}')
        plt.xlabel(feature_name)
        plt.ylabel('Partial Dependence')
        plt.title(f'Context-Aware PDP for {feature_name}')
        plt.legend()
        plt.show()
