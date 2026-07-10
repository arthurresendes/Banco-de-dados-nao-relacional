export const atualizarCast = async (dados) => {
  const URL = "http://localhost:8000/api/v1/atualizando";
  const res = await fetch(URL, {
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

  if (!res.ok) {
    throw new Error(`Erro insesperado. Código: ${res.status}`);
  }

  return await res.json();
};
