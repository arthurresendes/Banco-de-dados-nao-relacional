import { useEffect, useState } from 'react'
import { verTodosTipos } from '../api/getVerTodosTipos'
import { cadastrando } from '../api/cadastrarAluno'

const Cadastro = () => {
    const [nome, setNome] = useState("")
    const [tipo, setTipo] = useState("Action & Adventure")
    const [listaDeTipos, setListaDeTipos] = useState([])
    const [ano, setAno] = useState()
    const [raiting, setRaiting] = useState("")
    const [duration, setDuration] = useState("")
    const [description, setDescription] = useState("")
    const [cast, setCast] = useState([])
    const [paises, setPaises] = useState([])
    const [directors, setDirectors] = useState([])
    const [listed, setListed] = useState([])
    const [inputCast, setInputCast] = useState("")
    const [inputPaises, setInputPaises] = useState("")
    const [inputDirectors, setInputDirectors] = useState("")
    const [inputListed, setInputListed] = useState("")
    const [erro, setErro] = useState("")
    const [mensagem, setMensagem] = useState("")

    useEffect(() => {
        const buscarDados = async () => {
            const res = await verTodosTipos();
            setListaDeTipos(res);
        };
        buscarDados()
    }, [])

    const lidarComTeclado = (event, inputTexto, setInputTexto, lista, setLista) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            if (inputTexto.trim() === '') return;
            setLista((listaAnterior) => [...listaAnterior, inputTexto.trim()]);
            setInputTexto('');
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault()
        setMensagem("")
        setErro("")
        const dados = {
            tipo,
            nome,
            ano,
            raiting,
            duration,
            description,
            cast: inputCast.trim() ? [...cast, inputCast.trim()] : cast,
            paises: inputPaises.trim() ? [...paises, inputPaises.trim()] : paises,
            directors: inputDirectors.trim() ? [...directors, inputDirectors.trim()] : directors,
            listed: inputListed.trim() ? [...listed, inputListed.trim()] : listed
        }
        try {
            const cadastrar = await cadastrando(dados)
            setMensagem(cadastrar)
        } catch (e) {
            setErro(e.message)
        }

    }

    return (
        <div>
            <form action="" onSubmit={handleSubmit}>
                <label htmlFor="nome" className='nome'>
                    <span>Nome</span>
                    <input type="text" name="nome" id="nome" value={nome} onChange={(e) => setNome(e.target.value)} required />
                </label>

                <label>
                    <span>Tipo do filme</span>
                    <select name="tipo" id="" onChange={(e) => setTipo(e.target.value)} value={tipo}>
                        {listaDeTipos.map((lista) => (
                            <option key={lista} value={lista}>{lista}</option>
                        ))}
                    </select>
                </label>

                <label htmlFor="ano" className='ano'>
                    <span>Ano</span>
                    <input type="number" name="ano" id="ano" value={ano} onChange={(e) => setAno(e.target.value)} required />
                </label>

                <label htmlFor="raiting" className='raiting'>
                    <span>Rating</span>
                    <input type="text" name="raiting" id="raiting" value={raiting} onChange={(e) => setRaiting(e.target.value)} required />
                </label>

                <label htmlFor="duration" className='duration'>
                    <span>Duração</span>
                    <input type="text" name="duration" id="duration" value={duration} onChange={(e) => setDuration(e.target.value)} required />
                </label>

                <label htmlFor="description" className='description'>
                    <span>Descrição</span>
                    <input type="text" name="description" id="description" value={description} onChange={(e) => setDescription(e.target.value)} required />
                </label>

                <label htmlFor="cast" className='cast'>
                    <span>Elenco</span>
                    <span style={{ color: 'gray' }}>{cast.join(', ')}</span>
                    <input type="text" name="cast" id="cast" value={inputCast} onChange={(e) => setInputCast(e.target.value)} onKeyDown={(e) => lidarComTeclado(e, inputCast, setInputCast, cast, setCast)} />
                </label>

                <label htmlFor="paises" className='paises'>
                    <span>Países</span>
                    <span style={{ color: 'gray' }}>{paises.join(', ')}</span>
                    <input type="text" name="paises" id="paises" value={inputPaises} onChange={(e) => setInputPaises(e.target.value)} onKeyDown={(e) => lidarComTeclado(e, inputPaises, setInputPaises, paises, setPaises)} />
                </label>

                <label htmlFor="directors" className='directors'>
                    <span>Diretores</span>
                    <span style={{ color: 'gray' }}>{directors.join(', ')}</span>
                    <input type="text" name="directors" id="directors" value={inputDirectors} onChange={(e) => setInputDirectors(e.target.value)} onKeyDown={(e) => lidarComTeclado(e, inputDirectors, setInputDirectors, directors, setDirectors)} />
                </label>

                <label htmlFor="listed" className='listed'>
                    <span>Categorias</span>
                    <span style={{ color: 'gray' }}>{listed.join(', ')}</span>
                    <input type="text" name="listed" id="listed" value={inputListed} onChange={(e) => setInputListed(e.target.value)} onKeyDown={(e) => lidarComTeclado(e, inputListed, setInputListed, listed, setListed)} />
                </label>

                <input type="submit" value="Cadastrar" />
            </form>
            {mensagem != '' && (
                <div style={{ backgroundColor: "#dcfce7", color: "#166534", border: "1px solid #86efac", borderRadius: "8px", padding: "12px 16px", marginTop: "20px", textAlign: "center", fontWeight: 'bolder' }}>
                    <p style={{ margin: 0 }}>{mensagem}</p>
                </div>
            )}
            {erro != '' && (
                <div
                    style={{ backgroundColor: "#fee2e2", color: "#b91c1c", border: "1px solid #fca5a5", borderRadius: "8px", padding: "12px 16px", marginTop: "20px", textAlign: "center", fontWeight: 'bolder' }}>
                    <p style={{ margin: 0 }}>{erro}</p>
                </div>
            )}
        </div>
    )
}

export default Cadastro