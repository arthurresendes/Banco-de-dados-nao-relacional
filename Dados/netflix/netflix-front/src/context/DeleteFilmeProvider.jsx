import { createContext, useState } from "react";

export const DeleteFilme = createContext()

export const DeleteFilmeProvider = ({ children }) => {
    const [erro, setErro] = useState(null)
    const [excluir, setExcluir] = useState(false)
    const [busca, setBusca] = useState("")
    return (
        < DeleteFilme.Provider value={{ busca, setBusca, excluir, setExcluir, erro, setErro }}>
            {children}
        </DeleteFilme.Provider >
    )
}