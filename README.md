# crud-операции-fastapi
Использование Fast API для реализации общих кейсов
## Структура проекта
```
├── app
    ├── backend
        ├── db.py
        └── db_depends.py
    ├── migrations versions
        ├── versions
        ├── README
        ├── env.py
        └── script.py.mako
    ├── models
        ├── __init__.py
        ├── task.py
        └── user.py
    ├── routers
        ├── __init__.py
        ├── task.py
        └── user.py
    ├── __init__.py
    ├── main.py
    └── schemas.py
├── alembic.ini
├── requirements.txt
└── taskmanager.db
```

### Запуск:
```
cd app
python -m uvicorn main:app
```

### Команды alembic:
```alembic init app/migrations```: инициализация миграций<br>
```alembic revision --autogenerate -m "revision_name"```: создание новой миграции<br>
```alembic upgrage head```: применение миграции<br>
```alembic downgrade base```: откат миграции<br>

### Демонстрация:
<img src="https://github.com/KatKabaev/crud-operations-fastapi/blob/main/img1.png">
