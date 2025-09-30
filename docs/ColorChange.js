<script type="text/javascript" src="colorChange.js"></script>
window.addEventListener('DOMContentLoaded', init, false);

function init() {
    alert("The page loaded!");
}
<button>Change Color</button>
<button>Do Something Else</button>
function init() {
    var buttons = document.getElementsByTagName("button");
    buttons[0].addEventListener("click", changeColor, false);
    buttons[1].addEventListener("click", newFunction, false);
}

function changeColor() {
    var box = document.getElementById("colorToggle");
    box.style.backgroundColor = "skyblue";
}

function newFunction() {
    alert("Second button clicked!");
}
<div id="colorToggle" style="width:200px; height:200px; background-color:lightgray;"></div>
console.log("Testing…");