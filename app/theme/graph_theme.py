from matplotlib.axes    import Axes
from matplotlib.figure  import Figure

MEDIUM_DARK : str = "#191919"
MEDIUM_WHITE: str = "#D9D9D9"

def theme_romuro(ax: Axes, fig: Figure, xl: str, yl: str, t: str) -> None:
    ax.set_facecolor(MEDIUM_DARK)
    ax.set_xlabel(xl, color=MEDIUM_WHITE)
    ax.set_ylabel(yl, color=MEDIUM_WHITE)
    ax.tick_params(axis="both", color=MEDIUM_WHITE, labelcolor=MEDIUM_WHITE)
    ax.spines['bottom'].set_color(MEDIUM_WHITE)
    ax.spines['left'].set_color(MEDIUM_WHITE)
    ax.spines['top'].set_color(MEDIUM_DARK) 
    ax.spines['right'].set_color(MEDIUM_DARK)
    ax.set_title(t, color=MEDIUM_WHITE)
    
    fig.set_facecolor(MEDIUM_DARK)