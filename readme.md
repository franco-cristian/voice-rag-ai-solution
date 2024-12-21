# Voice RAG AI Solution

## Descripción del Proyecto

**Voice RAG AI Solution** es una solución avanzada que combina la funcionalidad de **voz a voz (V2V)** con el patrón **Retrieve-Augment-Generate (RAG)** para ofrecer respuestas contextuales precisas basadas en datos provenientes de múltiples fuentes. 

El proyecto integra:
1. **Azure OpenAI** para transcripción, generación de texto y síntesis de voz.
2. **Azure Cognitive Search** para búsqueda vectorial de documentos y fragmentos relevantes.
3. **Azure Blob Storage** para almacenamiento de datos como PDFs.
4. **API externa (AviationStack)** para consultar información de vuelos.
5. **Frontend interactivo** que permite consultas por voz y responde con texto y audio.

---

## Características Principales

1. **Consultas por voz**:
   - El usuario puede realizar preguntas hablando a través de un micrófono.
   - La IA convierte la voz a texto, busca información relevante y responde en texto y voz.

2. **RAG (Retrieve-Augment-Generate)**:
   - Obtiene datos relevantes desde múltiples fuentes:
     - PDFs y otros documentos almacenados en **Blob Storage**.
     - Información externa desde la API de **AviationStack**.
   - Combina los datos para generar respuestas contextuales.

3. **Respuesta en voz**:
   - La respuesta generada se sintetiza en audio utilizando **Azure OpenAI**.

---

## Requisitos del Sistema

### **Backend**
- **Python 3.9+**
- Azure Function App
- Azure Cognitive Search
- Azure Blob Storage
- Azure OpenAI
- API de AviationStack

### **Frontend**
- **Node.js** (versión 18+)
- React

---

## Estructura del Proyecto

