const URL = "http://localhost:8000/api/v1/see_especific";

export const buscaPorNome = async (name) => {
  const res = await fetch(`${URL}/${name}`);
  if (res.status === 404) {
    throw new Error("Filme não encontrado");
  }

  if (!res.ok) {
    throw new Error(`Erro ao encontrar o filme. Código: ${res.status}`);
  }
  const dados = await res.json();
  return dados;
};
