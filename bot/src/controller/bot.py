from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters
from src.handler.handlers import (
    start,
    date_chosen,
    input_date,
    select_option,
    option_chosen,
    cancel,
)
from src.model.conversation_state import (
    SELECT_DATE,
    INPUT_DATE,
    SELECT_OPTION,
    OPTION_CHOSEN,
)


def setup_bot(application):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, date_chosen)],
            INPUT_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_date)],
            SELECT_OPTION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, select_option)
            ],
            OPTION_CHOSEN: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, option_chosen)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
