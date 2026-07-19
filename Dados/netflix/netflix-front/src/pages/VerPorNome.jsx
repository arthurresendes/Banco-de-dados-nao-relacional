import React, { useContext } from 'react'
import { buscaPorNome } from '../api/getBuscaPorNome'
import { GetFilmeName } from '../context/GetFilmeNameProvider'

const VerPorNome = () => {
    const { busca, setBusca, res, setRes, erro, setErro } = useContext(GetFilmeName)
    const handleSearch = async (e) => {
        e.preventDefault()
        setRes([])
        setErro(null)
        try {
            const dados = await buscaPorNome(busca)
            setRes(dados)
        } catch (err) {
            setErro(err.message)
        }
    }
    return (
        <div>
            <form action="" onSubmit={handleSearch}>
                <label htmlFor="">
                    Nome do filme/série
                    <input type="text" name="" id="" value={busca} onChange={(e) => setBusca(e.target.value)} />
                    <input type="submit" value="Enviar" />
                </label>
            </form>
            <hr />
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
            {erro != null && <p style={{ color: 'red' }}>{erro}</p>}
        </div>
    )
}

export default VerPorNome