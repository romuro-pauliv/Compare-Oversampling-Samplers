from data.create_dataset    import CreateDataset
from graph.scatter          import Scatter
from graph.decision_funcion import DecisionFunction


from imblearn.over_sampling import SMOTE
from sklearn.svm            import SVR

import matplotlib.pyplot as plt


XY, S = CreateDataset.create(400, (0.9, 0.1), 2, 0.3, 2)


clf: SVR = SVR()
model = clf.fit(XY, S)
fig0, ax0 = plt.subplots()
Scatter(XY, S).scatter_graph(ax0, fig0, "BRUTE", 1)
DecisionFunction(XY, S, model, ax0, 0).plot()

fig1, ax1 = plt.subplots()
Scatter(XY, S).scatter_graph(ax1, fig1, "BRUTE", 1)
DecisionFunction(XY, S, model, ax1, 0.4).plot()

clf: SVR = SVR()

XY_res, S_res = SMOTE().fit_resample(XY, S)
model = clf.fit(XY_res, S_res)

fig2, ax2 = plt.subplots()
Scatter(XY, S).scatter_graph(ax2, fig2, "SMOTE", 1)
Scatter(XY_res, S_res).scatter_graph(ax2, fig2, "SMOTE", 0.4)
DecisionFunction(XY_res, S_res, model, ax2, 0).plot()

fig3, ax3 = plt.subplots()
Scatter(XY, S).scatter_graph(ax3, fig3, "SMOTE")
DecisionFunction(XY, S, model, ax3, 0.4).plot()

plt.show()