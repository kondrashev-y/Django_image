Репозиторий сервиса по загрузки изображения на Django 3.

Установка (для пользователей операционных систем семейства **MacOs/Linux**):

1. Открыть терминал или консоль и перейти в нужную Вам директорию
2. Прописать команду `git clone https://github.com/kondrashev-y/Django_image`
3. Прописать следующие команды:
- `python3 -m venv venv`
- `source venv/bin/activate`
-  Перейти в директорию **Django-image** `cd Django_image/`
- `pip install -r requirements.txt`
- `python manage.py migrate`
6. Добавить директорию **media**, куда будут сохраняться изображения `mkdir media`
5. Запустить сервер - `python manage.py runserver`
6. В браузере перейти по ссылке  http://127.0.0.1:8000/
