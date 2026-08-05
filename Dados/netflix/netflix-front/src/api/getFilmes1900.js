const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const verFilmes1900 = async (pagina = 1) => {
  const res = await fetch(
    `${URL}/api/v1/netflix_lt_2000_page?pagina=${pagina}`,
  );
  const dados = await res.json();
  return dados;
};
