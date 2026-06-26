import React, { useState } from 'react'
import { buscaPorAtor } from '../api/buscaPorAtor'

const VerSobreAtor = () => {
    const [busca, setBusca] = useState('')
    const [res, setRes] = useState([])
    const handleSearch = async (e) => {
        e.preventDefault()
        const dados = await buscaPorAtor(busca)
        setRes(dados)
    }
    return (
        <div>
            <form action="" onSubmit={handleSearch}>
                <label htmlFor="">
                    Nome do ator
                    <input type="text" name="" id="" value={busca} onChange={(e) => setBusca(e.target.value)} />
                    <input type="submit" value="Enviar" />
                </label>
            </form>

            {res && res.length > 0 && (
                <ul>
                    {res.map((filme) => (
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
            )}
        </div>
    )
}

export default VerSobreAtor