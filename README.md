# Telegram Bot

Учебный Telegram-бот на Python, созданный в рамках лабораторной работы № 5.

## Features

- `/start` — запуск бота и приветственное сообщение.
- `/help` — отображение списка доступных команд.

## Requirements

- Python 3
- pyTelegramBotAPI

## Installation and Setup

1. Install the required library:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Скопируйте `config.example.py` в `config.py`.

3. Вставьте свой токен в файл `config.py`.

4. Запустите бота:

   ```bash
   python bot.py
   ```

## Security

 `config.py` файл хранит в себе токен бота и его нельзя публиковать в гитхаб.