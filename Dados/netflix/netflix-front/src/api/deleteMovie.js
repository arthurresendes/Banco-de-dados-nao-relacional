export const deleteMovie = async (name) => {
  const URL = `http://localhost:8000/api/v1/delete_per_name/${name}`;
  const res = await fetch(URL, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (res.status === 404) {
    throw new Error("Filme não encontrado");
  }

  if (!res.ok) {
    throw new Error(`Erro insesperado. Código: ${res.status}`);
  }

  return true;
};
