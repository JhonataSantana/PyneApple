import os
import eel
from engine import *
from classes.utils import joinPath, explodePath
from pandas import DataFrame
from datetime import date
from classes.consolidador import Consolidador


def main2() -> None:

    # main_path: str = os.getcwd()
    
    # files_path: str = joinPath(explodePath('./files'))

    # init_date: date = date(2024, 3, 25)
    # end_date: date = date.today()
    # date_filter = (init_date, end_date, '%Y%m%d')

    # consolidated: DataFrame = Consolidador(files_path, substring='test', date_interval=date_filter).run()
    
    # final_filename: str = os.path.join(main_path, "consolidado.csv")
    # consolidated.to_csv(final_filename, encoding="UTF-8", sep=',', index=False)

    return


def main() -> None:
    eel.init('web')
    eel.start('index.html', size=(1280,720))


if __name__ == "__main__":
    main()

