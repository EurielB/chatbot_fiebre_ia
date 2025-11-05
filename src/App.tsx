import Chat from './components/Chat'

export default function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>🌡️ Agente sobre Fiebre</h1>
        <p className="subtitle">Pregúntame solo sobre fiebre. No sustituyo atención médica profesional.</p>
      </header>
      <main>
        <Chat />
      </main>
      <footer className="footer">
        <small>
          🔧 Backend: LM Studio | 🤖 Modelo: google/gemma-3-1b | 
          💻 Desarrollado con React + Vite
        </small>
      </footer>
    </div>
  )
}


