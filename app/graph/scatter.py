# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                               app/graph/scatter.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import matplotlib.pyplot    as plt
import seaborn              as sns
import numpy                as np

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from theme.graph_theme import theme_romuro
# |--------------------------------------------------------------------------------------------------------------------|

sns.set_context("paper")

class Scatter(object):
    def __init__(self, XY: np.ndarray, S: np.ndarray) -> None:
        """
        Initialize the Scatter instance.
        Args:
            XY (np.ndarray): [X, Y] array
            S (np.ndarray): Classe array. Ex.: [0, 0, 0, 1, 1, 2, 2, 2] for the 3 classes
        """
        self.XY: np.ndarray = XY
        self.S : np.ndarray = S
        
        self.p_alpha        : float = 0.8
        self.p_edgecolor    : str   = "k"
    
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
            
    def scatter_graph(self, ax: Axes, fig: Figure, title: str) -> None:
        """
        Creates the Scatter plot
        """
        theme_romuro(ax, fig, None, None, title)
        ax.scatter(
            self.XY[:, 0], self.XY[:, 1], c=self.new_s, alpha=self.p_alpha, edgecolors=self.p_edgecolor
        )
        ax.set_title(title)
        