import React, { useState } from 'react'
import { atualizarCast } from '../api/patchAtualizarCast'

const UpdateCast = () => {
    const [erro, setErro] = useState(null)
    const [busca, setBusca] = useState("")
    const [ator, setAtor] = useState("")
    const [mensagem, setMensagem] = useState("")

    const handleUpdate = async (e) => {
        e.preventDefault()
        setErro(null)
        setMensagem("")
        const payload = {
            nome: busca,
            ator: ator
        }
        try {
            const data = await atualizarCast(payload)
            setMensagem(data.Mensagem)
        } catch (err) {
            setErro(err.message)
        }
    }
    return (
        <div>
            <form action="" onSubmit={handleUpdate}>
                <label htmlFor="">
                    Nome do filme
                    <input type="text" name="" id="" value={busca} onChange={(e) => setBusca(e.target.value)} />
                </label>
                <br />
                <label htmlFor="">
                    Ator a ser adicionado
                    <input type="text" name="" id="" value={ator} onChange={(e) => setAtor(e.target.value)} />
                </label>
                <input type="submit" value="Enviar" />
            </form>

            <hr />
            {mensagem && <p style={{ color: 'green' }}>{mensagem}</p>}
            {erro != null && <p style={{ color: 'red' }}>{erro}</p>}
        </div>
    )
}

export default UpdateCast