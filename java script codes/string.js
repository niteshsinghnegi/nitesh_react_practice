// let name= "nitesh";
//  console.log(name.length)
//  console.log(name)

//  let love='manayata'
//  console.log(love)

//  let a = "nitesh "
//  let b = "manyata "
// let sentence=`${b} is a friend of ${a}`
// console.log(sentence)

// let c= 'bana\'na'
// console.log(c.length)

// let c1= 'mango\'is a famouse fruuiet'
// console.log(c1)

// string method 
// let fname="nitesh"+"negi"
// for (let charchater of fname){
//     console.log(charchater)
// }

// pracrice set 

let s = "nitesh"
console.log(s.endsWith("n"))

let s2 = "nitesh"
console.log(s2.startsWith("n"))
let name4="nitesh"
console.log(name4.toUpperCase())

let string="please give rs 1000"


let v=(string.slice("please give rs".length))
v=Number.parseInt(v)
console.log(v)
console.log(typeof v)

let str = "nitesh";
let result = "";

for (let i = 0; i < str.length; i++) {
    if (i === 3) {
        result += "X";
    } else {
        result += str[i];
    }
}

console.log(result);


