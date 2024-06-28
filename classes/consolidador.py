import os
import pandas as pd
from pandas import DataFrame
from datetime import datetime, date, timedelta

class Consolidador:

    def __init__(
            self, 
            folder_path: str, 
            file_types: str|list[str] = ['csv', 'xlsx'],
            substring: str|list[str] = '', 
            date_interval: tuple[date, date, str] = (),
            delimiter: str = None,
            separator: str = ',',
            enconding: str = 'UTF-8'
    ):
        
        self._folder_path = folder_path
        self._filters = {"substring": substring, 
                         "date_interval": date_interval}
        self._files =  self.applyFilters(self.getFiles(folder_path, file_types), self._filters)
        self._sep = separator
        self._delimiter = delimiter
        self._encoding = enconding


    def getFiles(self, path: str, file_types: list[str]) -> list[str]:

        file_types = [file_types] if type(file_types) == str else file_types
        file_types = [file_type.replace('.', '') for file_type in file_types]
        file_types = [f".{file_type}" for file_type in file_types]

        all_files: list[str] = os.listdir(path)

        return [file for file in all_files for file_type in file_types if file_type in file]


    def getData(self, file_path: str) -> DataFrame:
        data: DataFrame = DataFrame({})

        if ".csv" in file_path:
            data = pd.read_csv(file_path, sep=self._sep, delimiter=self._delimiter, encoding=self._encoding, index_col=False)
        elif ".xlsx" in file_path:
            data = pd.read_excel(file_path, index_col=False)

        return data


    def getFilesBySubstring(self, files: list[str], substring: str|list[str]) -> list[str]:
        
        substring_list: list[str] = [substring] if type(substring) == str else substring
        
        return [file for file in files for sub in substring_list if sub in file]
    

    def getFilesByDateInterval(self, files: list[str], date_filter: tuple[date, date, str]) -> list[str]:

        if date_filter[0] == '' and date_filter[1] == '':
            return files

        initial_date: date = date_filter[0] if date_filter[0] <= date_filter[1] else date_filter[1]
        end_date: date = date_filter[0] if date_filter[0] > date_filter[1] else date_filter[1]
        time_delta: date = (end_date - initial_date).days

        str_dates: list[str] = []

        for delta in range(time_delta + 1):
            current_date: date = initial_date + timedelta(delta)
            str_dates.append(current_date.strftime(date_filter[2]))
        
        return self.getFilesBySubstring(files, str_dates)


    def removeDuplicates(self, files: list[str]) -> list[str]:
        temp: list[str] = []
        
        for file in files: 
            if file not in temp:
                temp.append(file)

        return temp


    def applyFilters(self, files: list[str], filters: dict) -> list[str]:
        
        if filters['substring'] != '':
            files = self.getFilesBySubstring(files, filters["substring"])

        if len(filters["date_interval"]) != 0:
            files = self.getFilesByDateInterval(files, filters["date_interval"])

        return self.removeDuplicates(files)


    def consolidate(self) -> DataFrame:

        files: list[str] = self._files

        consolidated: DataFrame = DataFrame({})

        for filename in files:
            file_path: str = os.path.join(self._folder_path, filename)
            data: DataFrame = self.getData(file_path)
            consolidated = pd.concat([consolidated, data])

        consolidated.reset_index(inplace=True, drop=True)

        return consolidated
    

    def listFolderFiles(self) -> list[str]:
        return self._files


    def run(self) -> DataFrame:
        return self.consolidate()
    
