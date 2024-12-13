from app.backend.db import SessionLocal

async def get_db():
    """
    Функция-генератор для подключения к БД.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
