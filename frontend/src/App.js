import React, { useState } from "react";
import VoiceRecorder from "./VoiceRecorder";
import { sendAudioToBackend } from "./api";
import "./styles.css";

function App() {
  const [responseText, setResponseText] = useState("");
  const [isSpeaking, setIsSpeaking] = useState(false);

  const handleAudioUpload = async (audioBlob) => {
    setResponseText("Procesando tu consulta...");
    try {
      const audioResponse = await sendAudioToBackend(audioBlob);
      const audio = new Audio(URL.createObjectURL(audioResponse));
      setResponseText("Reproduciendo respuesta...");
      setIsSpeaking(true);
      audio.play();
      audio.onended = () => {
        setIsSpeaking(false);
        setResponseText("¡Consulta completada! Haz otra pregunta.");
      };
    } catch (error) {
      setResponseText("Hubo un error procesando tu consulta.");
    }
  };

  return (
    <div className="app-container">
      <h1>Bienvenido</h1>
      <p>Hazme tu pregunta</p>
      <VoiceRecorder onAudioUpload={handleAudioUpload} isSpeaking={isSpeaking} />
      <p className="response-text">{responseText}</p>
    </div>
  );
}

export default App;
