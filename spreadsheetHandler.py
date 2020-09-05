import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GSpreadWrapper:
  """This class wraps Google Sheet API calls to simplify operations
  It uses A1 notation
  """

  scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

  client = gspread.authorize(creds)

  def __init__(self, spreadSheet, workSheet):
    self.spreadSheet = GSpreadWrapper.client.open(spreadSheet)
    self.workSheet = self.spreadSheet.worksheet(workSheet)
  
  def get(self, cell):
    return self.workSheet.acell(cell).value

  def get_range(self, range):
    return self.workSheet.get(range)

  def find(self, value, in_row=None, in_col=None):
    cell = self.workSheet.find(value, in_row=in_row, in_column=in_col)
    return cell.row, cell.col

  def update(self, value, row, col):
    self.workSheet.update_cell(row, col, value)

  def check(self, row, col):
    self.workSheet.update_cell(row, col, 'TRUE')

  def uncheck(self, row, col):
    self.workSheet.update_cell(row, col, 'FALSE')