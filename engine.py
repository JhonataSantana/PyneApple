import eel
import json
import tkinter as tk
from datetime import date
from pandas import DataFrame
from tkinter import filedialog
from classes.consolidador import Consolidador


def treatDate(start_date: str, end_date: str):
    init_date: date = date.today()
    final_date: date = date.today()

    if start_date != '':
        split_date: list[str] = start_date.split('-')
        init_date = date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    if end_date != '':
        split_date: list[str] = end_date.split('-')
        final_date = date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    if start_date != '' and end_date == '':
        final_date = date.today()

    if start_date == '' and end_date != '':
        init_date = final_date
        final_date = date.today()

    date_filter: tuple[date, date, str] = (init_date, final_date, '%Y%m%d')

    if start_date == '' and end_date == '':
        date_filter = ()

    return date_filter


@eel.expose
def getOriginPath() -> str:
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    origin_path: str = filedialog.askdirectory(title="Selecione a pasta de origem")
    return origin_path


@eel.expose
def getFolderData(folder_path: str, substring: str, start_date: str, end_date: str) -> json:
    
    date_filter: tuple = treatDate(start_date, end_date)

    files: list[str] = Consolidador(folder_path, substring=substring, date_interval=date_filter).listFolderFiles()

    return files
