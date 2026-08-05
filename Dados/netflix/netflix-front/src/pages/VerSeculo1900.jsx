import React, { useContext, useEffect, useState } from 'react'
import { verFilmes1900 } from '../api/getFilmes1900'
import { GetAnos90 } from '../context/GetAnos90Provider'

const VerSeculo1900 = () => {
    const { dados, setDados, page, setPage, totalPage, setTotalPage, carregando, setCarregando } = useContext(GetAnos90)
    useEffect(() => {
        const buscarDados = async () => {
            const res = await verFilmes1900()
            setDados(res.Catalogo)
            setTotalPage(res.TotalPage)
        }
        buscarDados()
    }, [])

    const voltar = async () => {
        setCarregando(true)
        const novaPagina = page - 1
        setDados([])
        setPage(novaPagina)
        const res = await verFilmes1900(novaPagina)
        setDados(res.Catalogo)
        setCarregando(false)
    }
    const avancar = async () => {
        setCarregando(true)
        const novaPagina = page + 1
        setDados([])
        setPage(novaPagina)
        const res = await verFilmes1900(novaPagina)
        setDados(res.Catalogo)
        setCarregando(false)
    }
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
            {!carregando ? (
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', maxWidth: '960px', margin: '0 auto', padding: '0 24px' }}>
                    <button onClick={voltar} disabled={page === 1} className="btn-pagina">&lsaquo;</button>
                    <p style={{ margin: 0 }}>{page} / {totalPage}</p>
                    <button onClick={avancar} disabled={page === totalPage} className="btn-pagina">&rsaquo;</button>
                </div>
            ) : <p>Carregando...</p>}
        </div>
    )
}

export default VerSeculo1900