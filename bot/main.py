import logging
from telegram.ext import Application
from config import settings
from src.controller.bot import setup_bot

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main() -> None:
    application = Application.builder().token(settings.TELEGRAM_TOKEN).build()
    setup_bot(application)
    application.run_polling()


if __name__ == "__main__":
    main()
