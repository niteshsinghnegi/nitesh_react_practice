let num=prompt("enter your num ")
num=Number.parseInt(num)
if(num<4){
    location.href="https://www.google.com"
}

let colour=prompt("enter your colour ")
document.body.style.background=colour
console.log(document.body.firstChild)
console.log(document.body.lastChild)
// console.log(document.body.childNodes)

let arr = Array.from(document.body.childNodes)
console.log(arr)
