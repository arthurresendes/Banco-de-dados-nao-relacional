import { createContext, useState } from "react";

export const GetAnos90 = createContext()

export const GetAnos90Provider = ({ children }) => {
    const [dados, setDados] = useState([])

    return (
        < GetAnos90.Provider value={{ dados, setDados }}>
            {children}
        </GetAnos90.Provider >
    )
}