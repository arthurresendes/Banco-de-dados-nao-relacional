import React, { useContext, useState } from 'react'
import { deleteMovie } from '../api/deleteMovie'
import { DeleteFilme } from '../context/DeleteFilmeProvider'

const DeletarPorNome = () => {
    const { erro, setErro, excluir, setExcluir, busca, setBusca } = useContext(DeleteFilme)
    const handleDelete = async (e) => {
        e.preventDefault()
        setExcluir(false)
        setErro(null)
        try {
            await deleteMovie(busca)
            setExcluir(true)
        } catch (err) {
            setErro(err.message)
        }
    }
    return (
        <div>
            <form action="" onSubmit={handleDelete}>
                <label htmlFor="">
                    Nome do filme
                    <input type="text" name="" id="" value={busca} onChange={(e) => setBusca(e.target.value)} />
                    <input type="submit" value="Enviar" />
                </label>
            </form>

            <hr />
            {excluir && <p style={{ color: 'green' }}>Filme/Seríe excluido com sucesso</p>}
            {erro != null && <p style={{ color: 'red' }}>{erro}</p>}
        </div>
    )
}

export default DeletarPorNome