## Материалы по Python: примеры и шпаргалки

Набор коротких примеров на чистом Python: базовый синтаксис, структуры данных, функции, ООП, работа с файлами/путями/архивами, регулярки, JSON, `datetime`, стандартные модули, простая работа с БД SQLite, SMTP, и демо c `pipenv`.

### Что внутри
- `base/`: базовые конструкции и мини-примеры (функции, строки, операторы и т.д.)
- `extend/`:
  - `data_types/`: коллекции, числа, строки, диапазоны, распаковка
  - `data_types/classes/`: ООП (инкапсуляция, наследование, полиморфизм, абстракция)
  - `csv/`, `json/`, `files/`, `zip/`: работа с файлами и форматами
  - `regular_expressions/`: регулярные выражения
  - `sqlite/`: простые запросы к локальной `test.db`
  - `smtp_mail/`: отправка письма (нужны учётные данные)
  - `digits_modules/`: `math`, `random`, `secrets`
  - `pip-pyenv/`: пример использования `pipenv` и зависимостей

## Быстрый старт

Требуется установленный Python (рекомендую 3.11+). На macOS обычно команда `python3`.

```bash
# пример запуска любого файла
python3 base/hello.py
python3 extend/data_types/lists/main.py
python3 extend/regular_expressions/main.py
```

В большинстве примеров используются только стандартные библиотеки, ничего ставить не нужно.

### Виртуальное окружение (по желанию)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -V
```

## Доп. зависимости (демо с Pipenv)
В каталоге `extend/pip-pyenv/` есть `Pipfile` c примерами зависимостей (`requests`, `pygame`, `pandas`) и файл `req_test.py`.

```bash
cd extend/pip-pyenv
pipenv install
pipenv run python req_test.py  # или: pipenv shell && python req_test.py
```

Примечание: в `extend/pip-pyenv/Pipfile` указано `python_version = "3.14"`. Если у вас другая версия (например 3.12), поменяйте поле `python_version` на свою актуальную, либо установите соответствующую версию интерпретатора.

## Запуск отдельных примеров
```bash
# CSV/JSON
python3 extend/csv/main.py
python3 extend/json/main.py

# Работа с файлами и путями
python3 extend/files/main.py

# Архивы ZIP
python3 extend/zip/main.py

# SQLite (использует локальную extend/sqlite/test.db)
python3 extend/sqlite/main.py

# SMTP (перед запуском укажите реальные учётные данные внутри скрипта/переменных окружения)
python3 extend/smtp_mail/mail.py
```

## Частые вопросы/ошибки
- Pipenv требует другую версию Python: откройте `extend/pip-pyenv/Pipfile` и скорректируйте `python_version` под вашу установленную, затем снова `pipenv --rm && pipenv install`.
- macOS и SSL/сертификаты: если `requests` падает на SSL, обновите сертификаты (`Install Certificates.command` из каталога Python) или используйте системные серты (Homebrew Python обычно уже настроен).

## Лицензия/назначение
Учебные материалы и заготовки для быстрого повторения синтаксиса и стандартной библиотеки. Используйте свободно.