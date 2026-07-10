const URL = "http://127.0.0.1:8000/api/v1/netflix_lt_2000";

export const verFilmes1900 = async () => {
  const res = await fetch(URL);
  const dados = await res.json();
  return dados.Catalogo;
};
