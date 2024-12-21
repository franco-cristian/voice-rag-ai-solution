export const sendAudioToBackend = async (audioBlob) => {
  const formData = new FormData();
  formData.append("audio", audioBlob);

  const response = await fetch(process.env.REACT_APP_FUNCTION_URL, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Error al conectar con el backend");
  }

  return response.blob();
};
