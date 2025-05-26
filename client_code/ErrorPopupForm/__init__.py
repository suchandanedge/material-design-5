from ._anvil_designer import ErrorPopupFormTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class ErrorPopupForm(ErrorPopupFormTemplate):
  def __init__(self, error_items=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.data_grid_1.columns = [
      {"id": "display_name", "title": "Display Name", "data_key": "display_name", "width":150},
      {"id": "app_name", "title": "App Name", "data_key": "app_name", "width":150},
      {"id": "document_id", "title": "Document ID", "data_key": "document_id", "width":150},
      {"id": "log_time", "title": "Log Time", "data_key": "log_time", "width":120},
      {"id": "status_code", "title": "Status Code", "data_key": "status_code", "width":50},
      {"id": "error_text", "title": "Error Text", "data_key": "error_text", "width":150}
    ]
    self.repeating_panel_1.items = error_items
    
