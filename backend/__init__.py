import logging
import azure.functions as func
from v2v_rag import handle_voice_to_voice

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Procesando la solicitud...")

    try:
        # Leer archivo de audio enviado como multipart/form-data
        audio_file = req.files.get("audio")
        if not audio_file:
            return func.HttpResponse("Archivo de audio no proporcionado.", status_code=400)

        # Manejar flujo de Voz a Voz con RAG
        response_audio = handle_voice_to_voice(audio_file)

        # Retornar audio generado
        return func.HttpResponse(
            response_audio,
            mimetype="audio/wav",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Error interno: {str(e)}", status_code=500)
