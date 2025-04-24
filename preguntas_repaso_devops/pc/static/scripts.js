// Abrir ventanas flotantes en posiciones aleatorias
function openWindow(id) {
    let win = document.getElementById(id);
    win.style.display = "block";
    
    // Posicionar ventana en un lugar aleatorio dentro de la pantalla
    let maxX = window.innerWidth - win.clientWidth - 50;
    let maxY = window.innerHeight - win.clientHeight - 50;
    
    win.style.top = Math.max(50, Math.random() * maxY) + "px";
    win.style.left = Math.max(50, Math.random() * maxX) + "px";
}

// Cerrar ventanas flotantes
function closeWindow(id) {
    document.getElementById(id).style.display = "none";
}

// Hacer ventanas arrastrables con límites
document.querySelectorAll(".window").forEach(win => {
    let header = win.querySelector(".window-header");
    let offsetX, offsetY, isDragging = false;

    header.addEventListener("mousedown", e => {
        isDragging = true;
        offsetX = e.clientX - win.offsetLeft;
        offsetY = e.clientY - win.offsetTop;
        e.preventDefault(); // Prevenir selección de texto al arrastrar
    });

    document.addEventListener("mousemove", e => {
        if (isDragging) {
            let newX = e.clientX - offsetX;
            let newY = e.clientY - offsetY;

            // Limitar la ventana dentro de la pantalla
            let maxX = window.innerWidth - win.clientWidth;
            let maxY = window.innerHeight - win.clientHeight;

            win.style.left = Math.max(0, Math.min(newX, maxX)) + "px";
            win.style.top = Math.max(0, Math.min(newY, maxY)) + "px";
        }
    });

    document.addEventListener("mouseup", () => isDragging = false);
});

// Ejecutar comandos en la terminal
function runCommand() {
    let commandInput = document.getElementById("command-input");
    let command = commandInput.value.trim();

    if (command === "") return;

    fetch("/run-command", {
        method: "POST",
        body: JSON.stringify({ command: command }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        let output = document.getElementById("terminal-output");
        output.innerText += "\n$ " + command + "\n" + data.output;
        output.scrollTop = output.scrollHeight; // Auto-scroll hacia abajo
        commandInput.value = "";
    });
}

// Ejecutar comando con Enter
function handleKeyPress(event) {
    if (event.key === "Enter") {
        runCommand();
    }
}

// Actualizar reloj en la barra superior
function updateClock() {
    let now = new Date();
    let hours = now.getHours().toString().padStart(2, "0");
    let minutes = now.getMinutes().toString().padStart(2, "0");
    document.getElementById("clock").innerText = `🕒 ${hours}:${minutes}`;
}

// Actualizar la hora cada segundo
setInterval(updateClock, 1000);
updateClock(); // Llamar inmediatamente para mostrar la hora actual
