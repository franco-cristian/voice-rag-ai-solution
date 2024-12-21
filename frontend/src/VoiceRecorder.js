import React, { useRef, useState } from "react";

function VoiceRecorder({ onAudioUpload, isSpeaking }) {
  const mediaRecorderRef = useRef(null);
  const [isRecording, setIsRecording] = useState(false);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new MediaRecorder(stream);

    const chunks = [];
    mediaRecorderRef.current.ondataavailable = (event) => chunks.push(event.data);
    mediaRecorderRef.current.onstop = () => {
      const audioBlob = new Blob(chunks, { type: "audio/wav" });
      onAudioUpload(audioBlob);
    };

    mediaRecorderRef.current.start();
    setIsRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setIsRecording(false);
  };

  return (
    <div className="voice-recorder">
      <button
        onClick={isRecording ? stopRecording : startRecording}
        disabled={isSpeaking}
        className={isRecording ? "recording-button" : "microphone-button"}
      >
        {isRecording ? "Detener" : "🎤"}
      </button>
    </div>
  );
}

export default VoiceRecorder;
