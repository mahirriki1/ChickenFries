/**
 * Team idk yet -- Mahir Riki and Brian Chen
 * SoftDev2 pd2
 * K30 -- canvas based JS drawing
 * 2023-04-24m
 */


// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// init global state var
var mode = "rect";

// var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (e.target.innerHTML === "rect|circ") {
        e.target.innerHTML = "circle";
        mode = "circle";
    }
    else {
        e.target.innerHTML = "rect|circ";
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "purple";
    ctx.fillRect(mouseX, mouseY, 100, 150);
}

// var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
}

// var draw = function(e) {
var draw = (e) => {
    if (mode === "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

// var wipeCanvas = function() {
var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle") ;
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);