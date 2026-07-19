import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { GetFilmeNameProvider } from './context/GetFilmeNameProvider.jsx'
import { GetAnos90Provider } from './context/GetAnos90Provider.jsx'
import { GetNomeAtorProvider } from './context/GetNomeAtorProvider.jsx'
import { DeleteFilmeProvider } from './context/DeleteFilmeProvider.jsx'
import { PatchCastProvider } from './context/PatchCastProvider.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <GetFilmeNameProvider>
      <GetAnos90Provider>
        <GetNomeAtorProvider>
          <DeleteFilmeProvider>
            <PatchCastProvider>
              <App />
            </PatchCastProvider>
          </DeleteFilmeProvider>
        </GetNomeAtorProvider>
      </GetAnos90Provider>
    </GetFilmeNameProvider>
  </StrictMode>,
)
