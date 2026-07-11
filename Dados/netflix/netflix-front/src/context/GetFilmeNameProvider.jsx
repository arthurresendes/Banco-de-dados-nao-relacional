import { createContext, useState } from "react";

export const GetFilmeName = createContext()

export const GetFilmeNameProvider = ({ children }) => {
    const [busca, setBusca] = useState('')
    const [res, setRes] = useState([])
    const [erro, setErro] = useState(null)

    return (
        <GetFilmeName.Provider value={{ busca, setBusca, res, setRes, erro, setErro }}>
            {children}
        </GetFilmeName.Provider>
    )
}