from database import session_maker
from models import TradeResult

def save_data_to_db(data) -> None:

    print("Сохранение в базу данных...")
    with session_maker() as session:
        with session.begin():
            try:
                for item in data:
                    exchange_product_id = item["exchange_product_id"]
                    oil_id = exchange_product_id[:4]
                    delivery_basis_id = exchange_product_id[4:7]
                    delivery_type_id = exchange_product_id[-1]

                    trade_result = TradeResult(
                        exchange_product_id=exchange_product_id,
                        exchange_product_name=item["exchange_product_name"],
                        oil_id=oil_id,
                        delivery_basis_id=delivery_basis_id,
                        delivery_basis_name=item["delivery_basis_name"],
                        delivery_type_id=delivery_type_id,
                        volume=item["volume"],
                        total=item["total"],
                        count=item["count"],
                        date=item["date"],
                    )
                    session.add(trade_result)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e