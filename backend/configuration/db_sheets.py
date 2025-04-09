import gspread
import os
from google.oauth2.service_account import Credentials
from configuration.settings import Settings, settings

class GoogleSheet:
    def __init__(self, sheet_name: str, worksheet_name: str, settings: Settings):
        self.sheet_name = sheet_name
        self.worksheet_name = worksheet_name
        self.settings = settings
        self.client = self._auth()
        self.sheet = self.client.open(sheet_name).worksheet(worksheet_name)

    def _auth(self):
        credentials_path = self.settings.db.key_sheets
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        credentials = Credentials.from_service_account_file(
            credentials_path, scopes=scopes
        )
        return gspread.authorize(credentials)

    def get_all(self):
        return self.sheet.get_all_records()

    def append(self, row: list):
        self.sheet.append_row(row)

    def find_rows_by(self, column_name: str, value):
        data = self.get_all()
        return [row for row in data if str(row.get(column_name)) == str(value)]
