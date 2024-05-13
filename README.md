# API платформы торговой сети

Данный проект представляет собой API онлайн платформы торговой сети электроники.

## Технологии

- Python
- Django (Django REST framework)
- PostgresQL (БД для хранения данных)


## Запуск проекта на Windows:

1. Клонируйте репозиторий https://github.com/Sergo1613/Electronic_network.git на свой компьютер.
2. Перейдите в корневую директорию проекта
3. Cоздайте в ней и активируйте виртуальное окружение:
`python -m venv venv`  
`venv\Scripts\activate.bat`
4. Установите зависимости:  
`pip install -r requirements.txt`
5. Создайте .env файл в корневой директории проекта и заполните переменные из файла .env.sample.
6. Выполните миграции:  
`python manage.py migrate`
7. Создайте суперпользователя:  
`python manage.py csu`
8. Запустите проект:  
`python manage.py runserver`

## Документация API:

Документация API доступна после запуска сервера по адресу: http://127.0.0.1.8000/redoc/ или http://127.0.0.1:8000/swagger/