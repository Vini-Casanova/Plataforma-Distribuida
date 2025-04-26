import { useState } from "react";

export default function ComandoAtuador() {
  const [comando, setComando] = useState("");
  const [status, setStatus] = useState("null");

  const enviarComando = async () => {
    try {
      const resposta = await fetch("http://localhost:8080/enviar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ comando })
      });

      const data = await resposta.text();
      setStatus(`✅ Comando enviado: ${comando}`);
      setComando("");
    } catch (error) {
      console.error(error);
      setStatus("❌ Erro ao enviar comando.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">Controle de Atuadores</h1>
      <input
        type="text"
        value={comando}
        onChange={(e) => setComando(e.target.value)}
        placeholder="Digite o comando (ex: ligar luz)"
        className="p-2 border border-gray-400 rounded mb-4 w-full max-w-md"
      />
      <button
        onClick={enviarComando}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Enviar Comando
      </button>
      {status && <p className="mt-4 text-lg">{status}</p>}
    </div>
  );
}

