export const top5 = async (type) => {
  const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
  const res = await fetch(`${URL}/api/v1/especifics_types/${type}`);
  const dados = await res.json();
  return dados.Shows;
};
