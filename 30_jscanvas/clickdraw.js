// retrieve node in DOM via ID
var c = getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// init global state var
var mode = "rect";

// var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (e.innerHTML === "rect|circ") {
        e.innerHTML = "circle";
    }
    else {
        e.innerHTML = "rect|circ";
    }
}

var drawRect = function(e) {
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 100, 100);
}

// var drawCircle = function(e) {
var drawCircle = (e) = {

    console.log("mouseclick registered at ", mouseX, mouseY);

}

// var draw = function(e) {
var draw = (e) => {

}

// var wipeCanvas = function() {
var wipeCanvas = () => {

}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle") ;
bToggler.toggleMode;
var clearB = document.getElementById("buttonClear");
clearB.wipeCanvas;