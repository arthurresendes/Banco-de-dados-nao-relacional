import './App.css'
import VerTop5 from './pages/VerTop5'
import VerSeculo1900 from './pages/VerSeculo1900'

function App() {
  return (
    <>
      <h1>Top 5 filmes criminais Netflix</h1>
      <VerTop5 />
      <hr />
      <h1>Filmes do seculo 1900</h1>
      <VerSeculo1900 />
    </>
  )
}

export default App
