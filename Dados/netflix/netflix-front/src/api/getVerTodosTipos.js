const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
export const verTodosTipos = async () => {
  const res = await fetch(`${URL}/api/v1/see_all_types`);
  const dados = await res.json();
  return dados.Types;
};
