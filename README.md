# Приложение для заказа + табло

Сайт-портфолио с документацией курсового проекта «Приложение для заказа + табло» (программа OTUS «Системный аналитик. Advanced», автор — Липова Эльвира Евгеньевна).

Опубликованная документация: https://coffeeprograms.github.io/sa-coursework-restaurant/

Спецификация API лежит в репозитории: [docs/api/order_api.yaml](docs/api/order_api.yaml).

## Локальная сборка

Нужен Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Сайт откроется по адресу http://127.0.0.1:8000/

Проверка сборки без предупреждений:

```bash
mkdocs build --strict
```

## Публикация

При пуше в ветку `main` workflow «Публикация на GitHub Pages» собирает сайт и публикует его на GitHub Pages.

Перед первым деплоем источник Pages нужно один раз включить вручную:

1. Открыть репозиторий на GitHub.
2. Перейти в Settings, затем Pages.
3. В блоке Build and deployment в поле Source выбрать GitHub Actions.
4. Сохранить настройку, если GitHub показывает кнопку Save.

После слияния в `main` сайт будет доступен по адресу https://coffeeprograms.github.io/sa-coursework-restaurant/
