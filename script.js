const backendURL = "https://binario-vv94.onrender.com/";  //  URL de backend en Render

async function convertToBinary() {
    const text = document.getElementById("inputText").value;
    const response = await fetch(`${backendURL}/convert/text-to-binary`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById("result").innerText = "Binario: " + data.binary;
}

async function convertToText() {
    const binary = document.getElementById("inputText").value;
    const response = await fetch(`${backendURL}/convert/binary-to-text`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ binary })
    });
    const data = await response.json();
    document.getElementById("result").innerText = "Texto: " + data.text;
}
