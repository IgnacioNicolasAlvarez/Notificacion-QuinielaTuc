def format_results_for_telegram(results, chosen_option, selected_date):
    if not results:
        return "<pre>No hay resultados disponibles para esta fecha y opción.</pre>"

    message = f"🌟 <b>Opción Seleccionada:</b> <i>{chosen_option}</i>\n📅 <b>Fecha:</b> <i>{selected_date}</i>\n\n"
    message += "🏆 <b>Resultados del Sorteo:</b>\n\n"
    message += "<pre>Posición | Número\n-------- | ------</pre>\n"

    for result in results:
        formatted_position = str(result["posicion"] + 1).zfill(2)
        formatted_number = str(result["numero"]).zfill(4)

        if formatted_position == "01":
            message += f"<pre>🌟 {formatted_position} | {formatted_number}</pre>\n"
        else:
            extra_space = " " * 3
            message += (
                f"<pre>{extra_space}{formatted_position} | {formatted_number}</pre>\n"
            )

    return message
