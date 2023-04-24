// Team ----- :: Mahir Riki
// SoftDev pd2
// K29 -- Buttonation
// 2023-04-21w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


// When called, it adds to the bottom of the list "thelist"
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// removes an item at index n
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

// adds the red class to items in the list but does not overtake it if it already has a class
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

// adds either the red or blue class to items in the list based on number of items in list but does not overtake it if it already has a class
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
function fib(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
};

// FAC
function fac(n) {
  if (n == 0) {
    return 1;
  } else {
    return n * fac(n-1);
  }
};

// GCD
function gcd(a, b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a%b);
};

// buttons
function fibButton(n) {
  addItem("Fibonacci Calculation of " + n + ": " + fib(n));
}
function facButton(n) {
  addItem("Factorial Calculation of " + n + ": " + fac(n));
}
function gcdButton(a, b) {
  addItem("GCD Calculation of " + a + " and " + b + ": " + gcd(a, b));
}

// addItem("Fibonacci Calculation of 10: " + fib(10));
// addItem("Factorial Calculation of 10: " + fac(10));
// addItem("GCD Calculation of 10 and 5: " + gcd(10, 5));

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => { // this function syntax is a bit cleaner since it doesn't require the function keyword
  var retVal = fib(param1) + fac(param2) + gcd(param1, param2);
  return retVal;
};