import openai
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from ingest_data import extract_text_from_pdf
from aviation_api import get_flight_info
import wave
from io import BytesIO

def transcribe_audio(audio_file):
    """Convertir voz a texto usando OpenAI."""
    transcription = openai.Audio.transcribe(
        file=audio_file,
        model="whisper-1"
    )
    return transcription["text"]

def synthesize_audio(text, api_key, deployment_id):
    """Convertir texto a voz usando OpenAI Realtime."""
    openai.api_key = api_key
    response = openai.Audio.create(
        engine=deployment_id,
        prompt=text
    )
    return response["audio"]

def handle_voice_to_voice(audio_file):
    """Flujo Voz a Voz con RAG."""
    query = transcribe_audio(audio_file)

    # Caso 1: Consulta de vuelos
    if "vuelos" in query:
        cities = query.split("de")[1].split("a")
        origin, destination = cities[0].strip(), cities[1].strip()
        flight_info = get_flight_info(origin, destination)
        return synthesize_audio(flight_info, os.getenv("OPENAI_API_KEY"), os.getenv("VOICE_DEPLOYMENT_ID"))

    # Caso 2: Preguntas sobre un PDF
    if "manual" in query:
        pdf_text = extract_text_from_pdf("manual.pdf")
        prompt = f"""
        Texto del manual: {pdf_text}
        Pregunta: {query}
        """
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200
        )
        return synthesize_audio(response.choices[0].text, os.getenv("OPENAI_API_KEY"), os.getenv("VOICE_DEPLOYMENT_ID"))

    return synthesize_audio("Consulta no reconocida.", os.getenv("OPENAI_API_KEY"), os.getenv("VOICE_DEPLOYMENT_ID"))
