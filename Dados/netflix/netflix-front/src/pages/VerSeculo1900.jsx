import React, { useEffect, useState } from 'react'
import { verFilmes1900 } from '../api/filmes1900'

const VerSeculo1900 = () => {
    const [dados, setDados] = useState([])
    useEffect(() => {
        const buscarDados = async () => {
            const res = await verFilmes1900()
            setDados(res)
        }
        buscarDados()
    }, [])
    return (
        <div>
            <ul>
                {dados.map((filme) => (
                    <li key={filme._id}>
                        <h3>{filme.title} ({filme.type})</h3>
                        <p>Ano: {filme.release_year}</p>
                        <p>Duração: {filme.duration}</p>
                        <p>Classificação: {filme.rating}</p>
                        <p>Data adicionada: {filme.date_added}</p>
                        <p>Países: {filme.countries?.join(', ')}</p>
                        <p>Diretores: {filme.directors?.join(', ')}</p>
                        <p>Categorias: {filme.listed_in?.join(', ')}</p>
                        <p>Sinopse: {filme.description}</p>
                        <p>Elenco: {filme.cast?.join(', ')}</p>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default VerSeculo1900