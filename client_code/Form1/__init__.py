from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..ErrorPopupForm import ErrorPopupForm

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def button_1_click(self, **event_args):
    data = [
      {"display_name":"Orders", "app_name":"nsOrders", "document_id":"2035884", "log_time":"2025-05-14", "status_code":"404", "error_text":"error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
      {"display_name":"Refunds", "app_name":"nsRefunds", "document_id":"2035885", "log_time":"2025-05-15", "status_code":"404", "error_text":"error:error"},
    ]
    alert_form = ErrorPopupForm(data)
    alert(alert_form, large=True, title="Error Table")
