# Приложение для заказа + табло

Документация системы заказа для ресторана быстрого обслуживания: киоск самообслуживания, табло готовности и панель персонала.

Учебный проект курса OTUS «Системный аналитик. Advanced», защита 7 декабря 2026. Ресторан, цифры и сроки смоделированы.

Сайт: https://coffeeprograms.github.io/sa-coursework-restaurant/

## Что внутри

- Бизнес-требования, правила, нефункциональные требования и пользовательские истории
- Информационная модель и схемы C4 в PlantUML
- Спецификация OpenAPI 3.0.3 и Swagger UI: [docs/api/order_api.yaml](docs/api/order_api.yaml)
- Задачи, тест-кейсы и чек-лист приемки

## Автор

Липова Эльвира Евгеньевна, системный аналитик. 6 лет разработки на C# и 1 год системным аналитиком.

Telegram-канал: [Эльвира Липова · От требований к коду](https://t.me/lipova_ee)

## Стек документации

MkDocs Material, PlantUML, OpenAPI 3.0.3, GitHub Actions → Pages.

## Локальная сборка

Нужен Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Сайт откроется по адресу http://127.0.0.1:8000/

```bash
mkdocs build --strict
```
