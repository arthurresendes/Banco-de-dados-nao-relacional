import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { GetFilmeNameProvider } from './context/GetFilmeNameProvider.jsx'
import { GetAnos90Provider } from './context/GetAnos90Provider.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <GetFilmeNameProvider>
      <GetAnos90Provider>
        <App />
      </GetAnos90Provider>
    </GetFilmeNameProvider>
  </StrictMode>,
)
