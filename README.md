# foodgram-project-react ![example workflow](https://github.com/Jelister203/foodgram-project-react/actions/workflows/yamdb_workflow.yml/badge.svg)
### Описание
Учебный проект, задачей которого является настройка Github Actions.
### Технологии
Python 3.7
Django 2.2.19
### Шаблон заполнения env-файла
- Указываем, что работаем с PostgreSQL:
```
DB_ENGINE=django.db.backends.postgresql
```
- Указываем имя базы данных:
```
DB_NAME=postgres 
```
- Указываем логин для подключения к базе данных:
```
POSTGRES_USER=postgres
```
- Указываем пароль для подключения к БД:
```
POSTGRES_PASSWORD=postgres 
```
- Указываем название сервиса/контейнера:
```
DB_HOST=db 
```
- Указываем порт для подключения к БД:
```
DB_PORT=5432 
```
### Запуск проекта в dev-режиме
- Скопировать репозиторий на локальную машину:
```
git clone git@github.com:Jelister203/foodgram-project-react.git
```
- Перейти в директорию infra:
```
C:/.../foodgram-project-react/>cd infra
```
- Выполнить команду:
```
docker compose up -d --build
```
### Автор
Михаил Решетняк

### Дополнительно
- IP:
```
158.160.63.199
```
- Имя пользователя:
```
user
```
### Данные для входа в админку:
#### Логин
```
admin
```
#### Пароль
```
ebwervEgnabRom6
```