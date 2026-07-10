export const top5 = async (type) => {
  const URL = `http://localhost:8000/api/v1/especifics_types/${type}`;
  const res = await fetch(URL);
  const dados = await res.json();
  return dados.Shows;
};
