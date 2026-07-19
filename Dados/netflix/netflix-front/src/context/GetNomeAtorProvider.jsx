import { createContext, useState } from "react";

export const GetNomeAtor = createContext()

export const GetNomeAtorProvider = ({ children }) => {
    const [busca, setBusca] = useState('')
    const [res, setRes] = useState([])
    const [erro, setErro] = useState(null)
    return (
        < GetNomeAtor.Provider value={{ busca, setBusca, res, setRes, erro, setErro }}>
            {children}
        </GetNomeAtor.Provider >
    )
}