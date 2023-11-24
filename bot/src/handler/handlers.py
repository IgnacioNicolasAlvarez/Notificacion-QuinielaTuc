from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove

from datetime import datetime
from src.model.conversation_state import (
    SELECT_DATE,
    INPUT_DATE,
    SELECT_OPTION,
    OPTION_CHOSEN,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from src.database.persister import MongoDBPersister


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Hoy", "Elegir fecha"]]
    await update.message.reply_text(
        "¿De qué fecha quieres cargar la información?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return SELECT_DATE


async def date_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_choice = update.message.text
    if user_choice == "Hoy":
        today_date = datetime.now().strftime("%Y-%m-%d")
        context.user_data["selected_date"] = today_date
        await update.message.reply_text(f"Fecha seleccionada: {today_date}")
        return await select_option(update, context)
    elif user_choice == "Elegir fecha":
        await update.message.reply_text(
            "Por favor, ingresa la fecha en formato yyyy-mm-dd",
            reply_markup=ReplyKeyboardRemove(),
        )
        return INPUT_DATE
    return SELECT_OPTION


async def input_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    date_text = update.message.text
    context.user_data["selected_date"] = date_text
    return await select_option(update, context)


async def select_option(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [
        ["MATUTINO", "VESPERTINO", "DE LA SIESTA", "DE LA TARDE", "NOCTURNO"]
    ]
    await update.message.reply_text(
        "Elige una opción: MATUTINO, VESPERTINO, DE LA SIESTA, DE LA TARDE o NOCTURNO",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return OPTION_CHOSEN


async def option_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chosen_option = update.message.text
    selected_date = context.user_data.get(
        "selected_date"
    )  # Asegúrate de que esta clave coincida con la usada en otros handlers

    # Crear una instancia de MongoDBPersister y realizar una consulta
    mongo_persister = MongoDBPersister()
    results = mongo_persister.get_objects(selected_date, chosen_option)

    message = f"Opción seleccionada: {chosen_option}\nResultados:\n"
    for result in results:
        message += f"{result}\n"  # Formatea esto según la estructura de tus documentos en MongoDB

    await update.message.reply_text(message)

    mongo_persister.close_connection()  # Cerrar la conexión a la base de datos
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Operación cancelada.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
