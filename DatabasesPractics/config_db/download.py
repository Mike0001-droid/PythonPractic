import os
from datetime import date
import requests


def download_file(url: str, report_date: date, folder: str = "downloads"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{report_date}.xls"
    print(f"Загрузка файла: {filename} из {url}")
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        with open(filename, "wb") as f:
            f.write(content)
        print(f"Файл {filename} загружен")
    else:
         print(f"Ошибка загрузки {url}: HTTP {response.status_code}")