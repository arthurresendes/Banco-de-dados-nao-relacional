import React, { useEffect, useState } from 'react'
import { top5 } from '../api/top5'

const VerTop5 = () => {
    const [dados, setDados] = useState([])
    useEffect(() => {
        const buscarDados = async () => {
            const res = await top5();
            setDados(res);
        };
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

export default VerTop5