import React, { useEffect, useState } from "react";

function App() {
  const [score, setScore] = useState({ human: 0, machine: 0 });
  const [current, setCurrent] = useState(null); // { sequence, nextWord }
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState("");
  const [history, setHistory] = useState([]);
  const [gameOver, setGameOver] = useState(false);
  const [machineWord, setMachineWord] = useState("");

  // Cargar una nueva secuencia desde el backend
  const fetchNextSequence = () => {
    fetch("/nextword")
      .then((res) => res.json())
      .then((data) => {
        setCurrent({
          sequence: data.sequence,
          nextWord: data.next_word
        });
        setUserInput("");
        setResult("");
        setMachineWord("");
      });
  };

  // Al iniciar o al reiniciar, carga la primera secuencia
  useEffect(() => {
    fetchNextSequence();
    // eslint-disable-next-line
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!current) return;

    // Llama al backend Flask para la predicción de la máquina
    const response = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        seed_text: current.sequence,
        next_words: 1,
      }),
    });
    const data = await response.json();
    const machinePrediction = data.generated_text.trim().split(" ").pop().toLowerCase();
    const humanWord = userInput.trim().toLowerCase();
    const correctWord = current.nextWord.toLowerCase();

    let roundResult = "";
    let newScore = { ...score };

    if (humanWord === correctWord && machinePrediction === correctWord) {
      roundResult = "¡Empate! Ambos acertaron.";
      newScore.human += 1;
      newScore.machine += 1;
    } else if (humanWord === correctWord) {
      roundResult = "¡Punto para el humano!";
      newScore.human += 1;
    } else if (machinePrediction === correctWord) {
      roundResult = "¡Punto para la máquina!";
      newScore.machine += 1;
    } else {
      roundResult = `Nadie acertó. La respuesta era: "${correctWord}".`;
    }

    setResult(roundResult);
    setScore(newScore);
    setMachineWord(machinePrediction);
    setHistory([
      ...history,
      {
        sequence: current.sequence,
        human: humanWord,
        machine: machinePrediction,
        correct: correctWord,
        roundResult,
      },
    ]);

    if (newScore.human >= 3 || newScore.machine >= 3) {
      setGameOver(true);
    }
  };

  const handleNext = () => {
    fetchNextSequence();
    setResult("");
    setMachineWord("");
  };

  const handleRestart = () => {
    setScore({ human: 0, machine: 0 });
    setHistory([]);
    setGameOver(false);
    fetchNextSequence();
    setResult("");
    setMachineWord("");
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", fontFamily: "sans-serif" }}>
      <h1>¿Qué palabra sigue?</h1>
      <div>
        <strong>Marcador:</strong> Humano {score.human} - Máquina {score.machine}
      </div>
      {gameOver ? (
        <div>
          <h2>
            {score.human > score.machine
              ? "¡Ganó el humano! 🎉"
              : score.machine > score.human
              ? "¡Ganó la máquina! 🤖"
              : "¡Empate!"}
          </h2>
          <button onClick={handleRestart}>Jugar de nuevo</button>
        </div>
      ) : (
        <>
          <div style={{ margin: "2em 0" }}>
            <h3>Completa la secuencia:</h3>
            <div style={{ fontSize: "1.3em", marginBottom: 10, background: "#eee", padding: 10, borderRadius: 5 }}>
              {current ? current.sequence : "Cargando..."}
            </div>
            <form onSubmit={handleSubmit}>
              <input
                type="text"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="¿Qué palabra sigue?"
                required
                disabled={!!result}
              />
              <button type="submit" disabled={!!result || !current}>
                Enviar
              </button>
            </form>
            {result && (
              <div style={{ marginTop: 20 }}>
                <strong>{result}</strong>
                <br />
                <span>La máquina predijo: <b>{machineWord}</b></span>
                <br />
                <span>La palabra real era: <b>{current.nextWord}</b></span>
                <br />
                <button onClick={handleNext}>Siguiente secuencia</button>
              </div>
            )}
          </div>
        </>
      )}
      <hr />
      <div style={{ fontSize: "0.9em", color: "#888" }}>
        <strong>Historial de rondas:</strong>
        <ul>
          {history.map((h, i) => (
            <li key={i}>
              <b>{h.sequence} ___</b> | Humano: <i>{h.human}</i> | Máquina: <i>{h.machine}</i> | Correcta: <b>{h.correct}</b> | {h.roundResult}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App; 