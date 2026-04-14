// alert("Hello")
// console.log("Hey nitesh")
// let a1 =5
// let b =6
// console.log(a1+b)
// console.log(console)
// console.info('info')
// console.warn("warn")
// console.assert("err"==false)
// console.assert("err"!=false)
// console.error("err")
// alert("Enter the value of a!")
// let a = prompt("Enter a here", "578")
// a = Number.parseInt(a)
// alert("You entered a of type " + (typeof a))
// let write = confirm("Do you want to write it to the page")
// if (write) {
//   document.write(a)
// }
// else {
//   document.write("Please allow me to write")
// }

// console.log(window)
// window.console.log(window)
// console.log(document)
// document.body
// document.body.style.background="green"

// // question no : 1

// let runagain= true 
//  const candrive=(age)=>{
//   return age >=18 ? true:false

//  }
// while (runagain){
//   let age = prompt("enter your age ")
// age=Num<ber.parseInt(age)
// if (age< 0){
//   console.error("you can wrong input age ")
//   break;
// }
// if(candrive(age)){
//   alert("you can drive")
// }
// else {
//   alert("you can not drive") 
// }
//   runagain=confirm("do you want run again ")
// }

// // // question 2 

// Log the first child of the body
console.log(document.body.firstChild);           // Logs first child (could be a text node)
console.log(document.body.firstChild.nextSibling); // Logs second child (may still be text node)
console.log(document.body.children[0]);          // First element child
console.log(document.body.children[1]);          // Second element child

let z = document.body.firstChild;

console.log(z.parentNode);                       // Logs <body>
console.log(z.nodeType === Node.ELEMENT_NODE);   // true if z is an element node
console.log(z.firstChild.nextSibling);          // Next sibling of first child (likely the second child)
