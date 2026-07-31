export const atualizarCast = async (dados) => {
  const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
  const res = await fetch(`${URL}/api/v1/atualizando`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(dados),
  });

  if (res.status === 404) {
    throw new Error("Filme não encontrado");
  }

  if (res.status === 409) {
    throw new Error("Erro ao solicitar requisição. Aguarde!");
  }

  if (!res.ok) {
    throw new Error(`Erro insesperado. Código: ${res.status}`);
  }

  return await res.json();
};
