# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/data/create_dataset.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from sklearn.datasets import make_classification
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|


class CreateDataset(object):
    @staticmethod
    def create(n_samples: int, weigths: tuple[float], n_classes: int, 
               class_sep: float, n_clusters: int) -> tuple[np.ndarray]:
        """
        Generate a random n-class classification problem.
        Args:
            n_samples (int): The number of samples.
            weigths (tuple[float]): array-like of shape (n_classes,) or (n_classes - 1,)
            n_classes (int): The number of classes (or labels) of the classification problem.
            class_sep (float): The factor multiplying the hypercube size
            n_clusters (int): The number of clusters per class.

        Returns:
            tuple[np.ndarray]: 
            X ndarray of shape (n_samples, n_features) 
            The generated samples.

            y : ndarray of shape (n_samples,)
            The integer labels for class membership of each sample.
        """
        return make_classification(
            n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, 
            n_classes=n_classes, n_clusters_per_class=n_clusters, weights=list(weigths),
            class_sep=class_sep, random_state=0
        )