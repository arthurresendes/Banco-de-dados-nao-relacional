import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavBar from './components/NavBar'
import VerTop5 from './pages/VerTop5'
import VerSeculo1900 from './pages/VerSeculo1900'
import VerPorNome from './pages/VerPorNome'
import VerSobreAtor from './pages/VerSobreAtor'
import DeletarPorNome from './pages/DeletarPorNome'
import UpdateCast from './pages/UpdateCast'
import Cadastro from './pages/Cadastro'

function App() {
  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<VerTop5 />} />
        <Route path="/seculo-1900" element={<VerSeculo1900 />} />
        <Route path="/find-name" element={<VerPorNome />} />
        <Route path="/find-actor" element={<VerSobreAtor />} />
        <Route path="/delete-movie" element={<DeletarPorNome />} />
        <Route path="/update-cast" element={<UpdateCast />} />
        <Route path="/register" element={<Cadastro />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App