"""Иконки разделов левого меню, у которых нет собственной страницы."""

SECTION_ICONS = {
    "1. Бизнес-требования ко всему приложению": "material/silverware-fork-knife",
    "2. Задокументированные требования к приложению": "material/file-document-outline",
    "3. Спроектированная информационная модель": "material/graph-outline",
    "4. Спроектированная компонентная архитектура": "material/sitemap",
    "5. Спроектированный API": "material/api",
    "7. Описание критериев готовности и проверки требований": "material/clipboard-check-outline",
}


def on_nav(nav, config, files):
    for item in nav.items:
        icon = SECTION_ICONS.get(getattr(item, "title", None))
        if icon and not getattr(item, "meta", None):
            item.meta = {"icon": icon}
    return nav
