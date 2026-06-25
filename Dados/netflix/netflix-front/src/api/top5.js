const URL = "http://127.0.0.1:8000/api/v1/criminal_shows";

export const top5 = async () => {
  const res = await fetch(URL);
  const dados = await res.json();
  return dados.Shows;
};
