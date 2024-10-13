# Improved Telegram Bot

This project is based on the tutorial "Пишем Telegram Bot на Python / Создание ботов для начинающих за 30 минут" (Writing a Telegram Bot in Python / Creating bots for beginners in 30 minutes). The bot sends periodic messages asking if the user has programmed today.

## Improvements and Adaptations

1. **Updated to aiogram 3.x**: 
   - Replaced `executor` with asyncio for running the bot.
   - Updated decorator syntax from `@dp.message_handler` to `@dp.message`.
   - Implemented `Command("start")` as a filter for the start command.

2. **Asynchronous Sleep**: 
   - Replaced `time.sleep()` with `asyncio.sleep()` to avoid blocking the event loop.

3. **Enhanced Logging**: 
   - Fixed logging call from `logging.INFO` to `logging.info`.
   - Added basic logging configuration.

4. **Personalized Messages**: 
   - Added the user's name to the greeting message.
   - Included the user's name in the repeated messages.

5. **PowerShell Execution Policy (Windows Setup)**:
   - Instructions added for changing PowerShell execution policy to run scripts.

## Setup Instructions

### Windows PowerShell Setup

1. Open PowerShell as administrator.
2. Run the following command:
   ```
   Set-ExecutionPolicy RemoteSigned
   ```
3. Confirm the change by typing 'Y' when prompted.

### Project Setup

1. Clone this repository.
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.\.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file and add your Telegram Bot Token:
   ```
   TOKEN=your_bot_token_here
   ```
6. Run the bot:
   ```
   python bot.py
   ```

## Usage

After starting the bot, send the `/start` command in Telegram. The bot will greet you and then send a message asking if you've programmed today every 2 seconds, for a total of 10 messages.

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.
