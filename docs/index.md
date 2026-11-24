# Приложение для заказа + табло

Курсовой проект

по программе OTUS «Системный аналитик. Advanced»

на тему: «Приложение для заказа + табло»

Выполнила: Липова Эльвира Евгеньевна

2026

Telegram: [@lipova_ee](https://t.me/lipova_ee)

## [1.1. Объект автоматизации](01-biznes-trebovaniya/1.1-obekt-avtomatizacii.md)

Объект автоматизации — ресторан формата QSR (quick service restaurant, предприятие быстрого обслуживания) с самообслуживанием. В MVP гость оформляет заказ на киоске, при желании идентифицируется QR внешней системы лояльности, оплачивает заказ; кухня выполняет заказ, статус готовности отображается на табло. В Релизе 1 заказ доступен в мобильном приложении, в Релизе 2 — оценки, отзывы и отчеты. Границы проекта — в [разделе 1.6](01-biznes-trebovaniya/1.6-granicy.md).

## [1.2. Цели проекта](01-biznes-trebovaniya/1.2-celi-proekta.md)

Сократить очереди и время от выбора блюда до оплаты.

Снизить ошибки передачи заказа на кухню.

Обеспечить гостю понятный статус заказа до выдачи.

## Разделы

- [Глоссарий](glossariy.md)

1\. Бизнес-требования ко всему приложению

- [1.1. Объект автоматизации](01-biznes-trebovaniya/1.1-obekt-avtomatizacii.md)
- [1.2. Цели проекта](01-biznes-trebovaniya/1.2-celi-proekta.md)
- [1.3. Требования бизнеса](01-biznes-trebovaniya/1.3-trebovaniya-biznesa.md)
- [1.4. Метрики успеха](01-biznes-trebovaniya/1.4-metriki-uspeha.md)
- [1.5. Бизнес-процессы](01-biznes-trebovaniya/1.5-biznes-processy.md)
- [1.6. Границы](01-biznes-trebovaniya/1.6-granicy.md)

2\. Задокументированные требования к приложению

- [2.1. Назначение, границы и основания](02-trebovaniya/2.1-naznachenie-granicy-i-osnovaniya.md)
- [2.2. Роли и участники взаимодействия](02-trebovaniya/2.2-roli-i-uchastniki-vzaimodeystviya.md)
- [2.3. Ограничения и правила](02-trebovaniya/2.3-ogranicheniya-i-pravila.md)
- [2.4. Нефункциональные требования](02-trebovaniya/2.4-nefunkcionalnye-trebovaniya.md)
- [2.5. Пользовательские истории](02-trebovaniya/2.5-polzovatelskie-istorii.md)
- [2.6. Карта пользовательских историй](02-trebovaniya/2.6-karta-polzovatelskih-istoriy.md)

3\. Спроектированная информационная модель

- [3.1. Назначение модели](03-informacionnaya-model/3.1-naznachenie-modeli.md)
- [3.2. Диаграмма классов](03-informacionnaya-model/3.2-diagramma-klassov.md)
- [3.3. Описание сущностей](03-informacionnaya-model/3.3-opisanie-suschnostey.md)
- [3.4. Связи и кратность](03-informacionnaya-model/3.4-svyazi-i-kratnost.md)
- [3.5. Перечисления и статусные модели](03-informacionnaya-model/3.5-perechisleniya-i-statusnye-modeli.md)

4\. Спроектированная компонентная архитектура

- [4.1. Обоснование выбора архитектурного стиля](04-arhitektura/4.1-obosnovanie-vybora-arhitekturnogo-stilya.md)
- [4.2. Диаграмма компонентов](04-arhitektura/4.2-diagramma-komponentov.md)
- [4.3. Перечень интеграций](04-arhitektura/4.3-perechen-integraciy.md)
- [4.4. Схема и описание интеграции](04-arhitektura/4.4-shema-i-opisanie-integracii.md)

5\. Спроектированный API

- [5.1. Ресурсы и эндпоинты](05-api/5.1-resursy-i-endpointy.md)
- [5.2. Контракт метода POST /orders](05-api/5.2-kontrakt-metoda-post-orders.md)
- [5.3. Спецификация OpenAPI](05-api/5.3-specifikaciya-openapi.md)
- [5.4. Описание UI и взаимодействие с API](05-api/5.4-opisanie-ui-i-vzaimodeystvie-s-api.md)

- [6. Декомпозированные до задач требования](06-zadachi/index.md)
    - [6.1. Критерии готовности к разработке (DoR)](06-zadachi/6.1-kriterii-gotovnosti-k-razrabotke-dor.md)
    - [6.2. Критерии выполнения истории (DoD)](06-zadachi/6.2-kriterii-vypolneniya-istorii-dod.md)
    - [6.3. Истории MVP](06-zadachi/6.3-istorii-mvp.md)
    - [6.4. Истории Релиза 1](06-zadachi/6.4-istorii-reliza-1.md)
    - [6.5. Истории Релиза 2](06-zadachi/6.5-istorii-reliza-2.md)

7\. Описание критериев готовности и проверки требований

- [7.1. Подход к проверке](07-proverka/7.1-podhod-k-proverke.md)
- [7.2. Тест-кейсы MVP](07-proverka/7.2-test-keysy-mvp.md)
- [7.3. Тест-кейсы Релиза 1](07-proverka/7.3-test-keysy-reliza-1.md)
- [7.4. Чек-лист приемки](07-proverka/7.4-chek-list-priemki.md)

- [Приложение А. Исходники схем](prilozhenie-a.md)

## Спецификация API

[5.3. Спецификация OpenAPI](05-api/5.3-specifikaciya-openapi.md)

[Скачать order_api.yaml](api/order_api.yaml)
