const URL = "http://127.0.0.1:8000/api/v1/see_all_types"

export const verTodosTipos = async () => {
    const res = await fetch(URL)
    const dados = await res.json()
    return dados.Types
}