# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                     app/graph/decision_function.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
from matplotlib.axes import Axes
from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|


class DecisionFunction(object):
    def __init__(self, XY: np.ndarray, S: np.ndarray, model: Any, ax: Axes, alpha: float = 0.2) -> None:
        """
        Initialize the DecisionFunction instance.
        Args:
            XY (np.ndarray): The (X, Y) data
            S (np.ndarray): The class discriminator
        """
        self.XY     : np.ndarray    = XY
        self.S      : np.ndarray    = S
        self.model  : Any           = model
        self.ax     : Axes          = ax
        self.alpha  : float         = alpha
        
        self.plot_step: float = 0.2

        self.color_list     : list[str] = ["#3CC9B0", "#C9633C", "#C9C63C", "#783CC9"]
        self._convert_color()

    def _convert_color(self) -> None:
        """
        Convert to specified color the S data
        """
        self.new_s: list[str] = []
        for i in self.S:
            try:
                self.new_s.append(self.color_list[i])
            except IndexError:
                print("need more color in self.color_list")
                exit()
        
    def _define_threshold(self) -> None:
        self.x_min, self.x_max = self.XY[:, 0].min() - 1, self.XY[:, 0].max() + 1
        self.y_min, self.y_max = self.XY[:, 1].min() - 1, self.XY[:, 1].max() + 1
    
    def _get_new_xy(self) -> None:
        self.xx, self.yy = np.meshgrid(
            np.arange(self.x_min, self.x_max, self.plot_step), np.arange(self.y_min, self.y_max, self.plot_step)
        )
        self.new_xy: np.ndarray = np.c_[self.xx.ravel(), self.yy.ravel()]
        
    def _get_z(self) -> None:
        self.Z: np.ndarray = self.model.predict(self.new_xy)
        self.Z: np.ndarray = self.Z.reshape(self.xx.shape)
        
    def _create_countour(self) -> None:
        self.ax.contourf(self.xx, self.yy, self.Z, alpha=self.alpha)
    
    def _create_scatter(self) -> None:
        self.ax.scatter(self.XY[:, 0], self.XY[:, 1], c=self.new_s, alpha=0.2)
    
    def plot(self) -> None:
        self._define_threshold(), self._get_new_xy(), self._get_z()
        self._create_countour()