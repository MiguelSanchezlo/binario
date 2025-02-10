const backendURL = "https://binario-vv94.onrender.com/";  // URL de backend en Render

async function convertToBinary() {
    const text = document.getElementById("inputText").value;
    if (!text.trim()) {
        document.getElementById("result").innerText = "⚠️ Ingresa un texto válido.";
        return;
    }
    
    try {
        const response = await fetch(`${backendURL}/convert/text-to-binary`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        if (!response.ok) throw new Error("Error en la conversión.");

        const data = await response.json();
        document.getElementById("result").innerText = "Binario: " + data.binary;
    } catch (error) {
        document.getElementById("result").innerText = "❌ Error al convertir.";
    }
}

async function convertToText() {
    const binary = document.getElementById("inputText").value;
    if (!binary.trim()) {
        document.getElementById("result").innerText = "⚠️ Ingresa un binario válido.";
        return;
    }

    try {
        const response = await fetch(`${backendURL}/convert/binary-to-text`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ binary })
        });

        if (!response.ok) throw new Error("Error en la conversión.");

        const data = await response.json();
        document.getElementById("result").innerText = "Texto: " + data.text;
    } catch (error) {
        document.getElementById("result").innerText = "❌ Error al convertir.";
    }
}
