from azure.storage.blob import BlobServiceClient
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def extract_text_from_pdf(blob_name):
    """Extraer texto de PDFs usando Azure Form Recognizer."""
    form_recognizer_client = DocumentAnalysisClient(
        endpoint=os.getenv("FORM_RECOGNIZER_ENDPOINT"),
        credential=AzureKeyCredential(os.getenv("FORM_RECOGNIZER_KEY"))
    )
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
    blob_client = blob_service_client.get_blob_client(container="data", blob=blob_name)
    pdf_data = blob_client.download_blob().readall()

    poller = form_recognizer_client.begin_analyze_document("prebuilt-layout", pdf_data)
    result = poller.result()

    return " ".join([line.content for page in result.pages for line in page.lines])
