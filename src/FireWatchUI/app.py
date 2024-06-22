import faicons as fa
import plotly.express as px
from pathlib import Path

# Load data and compute static values
#from shared import app_dir, tips
#from shinywidgets import render_plotly

from shiny import reactive, render
from shiny.express import input, ui

ui.page_opts(title="EVFD", fillable=True)
ui.include_css( Path(__file__).parent / "stylesheets/styles.css")
