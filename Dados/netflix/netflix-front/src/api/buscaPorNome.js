const URL = "http://127.0.0.1:8000/api/v1/see_especific";

export const buscaPorNome = async (name) => {
  const res = await fetch(`${URL}/${name}`);
  const dados = await res.json();

  return dados;
};
