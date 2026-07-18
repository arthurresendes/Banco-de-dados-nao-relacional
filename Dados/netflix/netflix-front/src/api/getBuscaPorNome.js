const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
export const buscaPorNome = async (name) => {
  const res = await fetch(`${URL}/api/v1/see_especific/${name}`);
  if (res.status === 404) {
    throw new Error("Filme não encontrado");
  }

  if (!res.ok) {
    throw new Error(`Erro ao encontrar o filme. Código: ${res.status}`);
  }
  const dados = await res.json();
  return dados;
};
