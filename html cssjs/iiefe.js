// let p= ()=>{ return new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve("nitesh")
//     },4000)
// })
// }

//  (async()=>{
//   let p1= await p()
//   console.log(p1)
//   let p2= await p()
//    console.log(p2)
//   let p3= await p()
//    console.log(p3)
//  })()

//  destructuring ...............................//

// let arr=[12,24,54,67,56,453,]
// let [a,b,c,...rest]=arr
// console.log(a,b,c,rest)


// let{d,e}= {d:7,e:4}
// console.log(d,e)

// spread oprator//
// let arr1=[9,8,7]
// let obj1={...arr1}
// console.log(obj1)

// function multiplication(v1,v2,v3){
//     return v1*v2*v3
// }
// console.log(multiplication(2,3,4))

// let obj2={
//     name:"harshit",
//     age:34,
//     domain:"data science"
// }
// console.log({...obj2, name:"nitesh"})

//  local and global variable scope 

// {let j= 8
// }
// console.log(j)   //it gives an errror becouse let scope is in the blocks only we use var 

// {var m= 6
// }
// console.log(m)

// clouseres in java script 

// function init() {
//   var name = "Mozilla"; // name is a local variable created by init
//   function displayName() {
//     // displayName() is the inner function, that forms a closure
//     console.log(name); // use variable declared in the parent function
//   }
//   displayName();
// }
// init();

// arrow function 
