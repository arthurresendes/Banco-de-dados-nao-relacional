import React, { useEffect, useState } from 'react'
import { top5 } from '../api/top5'
import { verTodosTipos } from '../api/verTodosTipos'

const VerTop5 = () => {
    const [dados, setDados] = useState([])
    const [type, setType] = useState("Action & Adventure")
    const [result, setResult] = useState([])
    useEffect(() => {
        const buscarDados = async () => {
            const res = await verTodosTipos();
            setDados(res);
        };
        buscarDados()
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const listagem = await top5(type)
        setResult(listagem)
    }
    return (
        <div>
            <form action="" onSubmit={handleSubmit}>
                <select name="" value={type} id="" onChange={(e) => setType(e.target.value)}>
                    {dados.map((tipos) => (
                        <option value={tipos}>{tipos}</option>
                    ))}
                </select>
                <input type="submit" value="Validar" />
            </form>
            <ul>
                {result.map((filme) => (
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