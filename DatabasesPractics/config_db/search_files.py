from datetime import datetime
from download import download_file
from fetch_page import fetch_page, get_report_links
from DatabasesPractics.config_db.extract_report_data import extract_report_data



BASE_URL = "https://spimex.com/markets/oil_products/trades/results/"


def scrape_reports(start: int = 1, end: int = 365):
    print("Начало парсинга...")

    files = []
    all_data = []
    link_date_map = {}

    for page in range(start, end + 1):
        page_url = f"{BASE_URL}?page=page-{page}"
        page_html = fetch_page(page_url)
        report_links_and_dates = get_report_links(page_html)
        for link, date in report_links_and_dates:
            if date.year >= 2023:
                link_date_map[link] = date
                file = download_file(link, date)
                files.append(file)

        print("Извлечение данных...")
        for link, date in link_date_map.items():
            file_path = f"downloads/{date}.xls"
            report_data = extract_report_data(file_path)
            for item in report_data:
                item["date"] = date
                item["created_on"] = datetime.now()
                item["updated_on"] = datetime.now()
            all_data.extend(report_data)

    return all_data
