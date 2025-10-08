// Run init after page loads
window.addEventListener('DOMContentLoaded', init, false);

function init() {
    console.log("The page loaded!");
    
    // Attach events to buttons
    document.getElementById("colorBtn").addEventListener("click", changeColor, false);
    document.getElementById("darkModeBtn").addEventListener("click", toggleDarkMode, false);
    document.getElementById("alertBtn").addEventListener("click", newFunction, false);
    
    // Check saved dark mode preference
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }
}

// Change box color
function changeColor() {
    let box = document.getElementById("colorToggle");
    box.style.backgroundColor = (box.style.backgroundColor === "skyblue") ? "lightgray": "skyblue";
}

// Toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    
    // Save preference
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Example of a second button action
function newFunction() {
    alert("Second button clicked!");
}
let hoverBox = document.getElementById("hoverBox");
hoverBox.addEventListener("mouseover", () => {
    hoverBox.style.backgroundColor = "lightgreen";
    hoverBox.textContent = "Nice! You hovered!";
});
hoverBox.addEventListener("mouseout", () => {
    hoverBox.style.backgroundColor = "lightgray";
    hoverBox.textContent = "Hover over me!";
});
let count = 0;
document.getElementById("increaseBtn").addEventListener("click", () => {
    count++;
    document.getElementById("counterValue").textContent = count;
});
document.getElementById("decreaseBtn").addEventListener("click", () => {
    count--;
    document.getElementById("counterValue").textContent = count;
});
document.getElementById("secretCheck").addEventListener("change", function () {
    let message = document.getElementById("secretMessage");
    message.classList.toggle("hidden");
});

// --- Rocket Launch Animation ---
const rocket = document.getElementById("rocketSVG");
rocket.addEventListener("click", () => {
    rocket.classList.toggle("launch");
    
    const flame = document.getElementById("flame");
    flame.setAttribute("fill", flame.getAttribute("fill") === "orange" ? "red": "orange");
});

document.addEventListener("DOMContentLoaded", () => {
    const circle = document.querySelector("#colorCircle circle");
    circle.addEventListener("click", () => {
        const randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
        circle.setAttribute("fill", randomColor);
    });
});