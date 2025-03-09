from search_files import scrape_reports
from save_to_db import save_data_to_db
from database import Base
from database import engine


Base.metadata.create_all(engine)


if __name__ == '__main__':
    report_data = scrape_reports()
    save_data_to_db(report_data)
    print("Сохранение прошло успешно")