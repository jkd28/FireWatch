import faicons as fa
import pandas as pd
import plotly.express as px
from pathlib import Path

# Load data and compute static values
#from shared import app_dir, tips
#from shinywidgets import render_plotly

from shiny import reactive, render
from shiny.express import input, ui

app_dir = Path(__file__).parent

ui.page_opts(title="EVFD", fillable=True)
all_logged_data = pd.read_csv(app_dir / "../../data/LOG_ENTRIES.csv")

with ui.layout_columns(fill = False):
  with ui.card(full_screen=True):
    ui.card_header("Logged Data")

    @render.data_frame
    def table():
      return render.DataGrid(get_all_logged_data())
    
ui.include_css( app_dir / "stylesheets/styles.css")


# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------


@reactive.calc
def get_all_logged_data():
    return all_logged_data

