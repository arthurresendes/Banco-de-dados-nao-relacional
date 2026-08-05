import { createContext, useState } from "react";

export const GetAnos90 = createContext()

export const GetAnos90Provider = ({ children }) => {
    const [dados, setDados] = useState([])
    const [page, setPage] = useState(1)
    const [totalPage, setTotalPage] = useState()
    const [carregando, setCarregando] = useState(false)

    return (
        < GetAnos90.Provider value={{ dados, setDados, page, setPage, totalPage, setTotalPage, carregando, setCarregando }}>
            {children}
        </GetAnos90.Provider >
    )
}