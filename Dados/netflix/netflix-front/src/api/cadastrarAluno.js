const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const cadastrando = async (dados) => {
  const res = await fetch(`${URL}/api/v1/adicionando_novo`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dados),
  });

  if (res.status === 409) {
    throw new Error("Erro ao solicitar requisição. Aguarde!");
  }

  if (!res.ok) {
    throw new Error(`Erro insesperado. Código: ${res.status}`);
  }
  const result = await res.json();
  return result.Mensagem;
};
