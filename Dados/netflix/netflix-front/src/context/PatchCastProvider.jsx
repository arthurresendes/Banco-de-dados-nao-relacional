import { createContext, useState } from "react";

export const PatchCast = createContext()

export const PatchCastProvider = ({ children }) => {
    const [erro, setErro] = useState(null)
    const [busca, setBusca] = useState("")
    const [ator, setAtor] = useState("")
    const [mensagem, setMensagem] = useState("")
    return (
        < PatchCast.Provider value={{ busca, setBusca, erro, setErro, ator, setAtor, mensagem, setMensagem }}>
            {children}
        </PatchCast.Provider >
    )
}