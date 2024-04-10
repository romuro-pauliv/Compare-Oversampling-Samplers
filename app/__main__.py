from data.create_dataset import CreateDataset
from graph.scatter import Scatter

import matplotlib.pyplot as plt

XY, S = CreateDataset.create(400, (0.1, 0.3, 0.97), 3, 0.8, 1)

fig, ax = plt.subplots()

Scatter(XY, S).scatter_graph(ax, fig, "test")


plt.show()