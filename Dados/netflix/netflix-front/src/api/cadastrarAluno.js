const URL = "http://localhost:8000/api/v1/adicionando_novo";

export const cadastrando = async (dados) => {
  const res = await fetch(URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dados),
  });

  if (!res.ok) {
    throw new Error(`Erro insesperado. Código: ${res.status}`);
  }
  const result = await res.json();
  return result.Mensagem;
};
