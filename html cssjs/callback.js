// ex of syncronuse programing 
// let a=prompt("what is your name ")
// let c=prompt("what is your father name ")
// let b=prompt("what is your mother name  ")

// console.log("my name is "+a+"my fathername is "+c+"my mother name is "+b)

// asynronous
// console.log("start")
// setTimeout(function() {
// console.log("hey i am good ")
    
// },300
// )
// console.log("end")

function loadscript(src, callback) {
    let script = document.createElement('script');
    script.src = src;

    script.onload = function () {
        console.log("Script loaded: " + src);
        callback(src);   // ✅ success ke baad callback
    };

    script.onerror = function () {
        console.log("Error loading script: " + src);
    };

    document.body.appendChild(script);
}

function hello(src) {
    alert("Hello "+src);
}

function goodmorning(src) {
    alert("Hi Good Morning "+src);
}

// real JS file
loadscript(
    "https://cdnjs.cloudegflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js",
    hello
);
