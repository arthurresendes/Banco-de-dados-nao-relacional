const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const buscaPorAtor = async (name) => {
  const res = await fetch(`${URL}/api/v1/see_actor_especific/${name}`);
  if (res.status === 404) {
    throw new Error("Ator não encontrado");
  }

  if (!res.ok) {
    throw new Error(`Erro não identificado. Código: ${res.status}`);
  }
  const dados = await res.json();
  return dados.Aparições;
};
