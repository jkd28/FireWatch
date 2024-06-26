import faicons as fa
import pandas as pd
import plotly.express as px
from pathlib import Path
from vars import LogColumn

# Load data and compute static values
#from shared import app_dir, tips
#from shinywidgets import render_plotly

from shiny import reactive, render
from shiny.express import input, ui

app_dir = Path(__file__).parent

ui.page_opts(title="EVFD", fillable=True)
all_logged_data = pd.read_csv(app_dir / "../../data/LOG_ENTRIES.csv")

with ui.sidebar():
  ui.input_date_range("daterange", "Date range", start="2023-01-01", format="mm/dd/yyyy")  

with ui.layout_columns(fill = True):
  with ui.card(full_screen=True):
    ui.card_header("Logged Data")

    @render.data_frame
    def table():
      return render.DataGrid(get_date_limited_data())
    
ui.include_css( app_dir / "stylesheets/styles.css")


# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------
@reactive.calc
def get_all_logged_data():
    return all_logged_data

@reactive.calc
def get_date_limited_data():
   all_logged_data['event_date_obj'] = pd.to_datetime(all_logged_data[LogColumn.EventDate], format='%m/%d/%Y')
   mask = (all_logged_data['event_date_obj'].dt.date >= input.daterange()[0]) & (all_logged_data['event_date_obj'].dt.date < input.daterange()[1])
   return all_logged_data.loc[mask]
