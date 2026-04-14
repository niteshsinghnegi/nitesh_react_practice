// let p1 = new Promise(function (resolve, reject) {
//     console.log("my brother name is abhishek ")
//     setTimeout(()=>{
// console.log("i am promise and i am resolve")
// resolve(true)
// },5000)
// })

// let p2 = new Promise(function (resolve, reject) {
//     console.log("my brother name is abhishek ")
//     setTimeout(()=>{
// console.log("i am promise and i am rejected")
// reject(new error("i am an error"))
// },5000)
// })

// p1.then((value)=>{
//     console.log(value)
// })
// p2.catch((error)=>{
//     console.log("some error an occcured")
// })

// p2.then((value)=>{
//     console.log(value)
// },(error)=>{
//     console.log(error)
// },)

// let p3= new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//      console.log("my name is nitesh")   
//     },5000)
//     resolve(45)
    
// })
// p3.then((value)=>{
// console.log(value)
// let p4=new Promise((resolve,reject)=>{
//     setTimeout(() => {
//       resolve("my love is manayta")  
//     }, 2000);
    
// })
//    return p4

// }).then ((value)=>{
// console.log("i am java devloper")
// return 10
// }).then((value)=>{
// console.log("now we are data sciectist")
// })
const loadscript = (src) => {
    return new Promise((resolve, reject) => {

        let script = document.createElement("script");
        script.type = "text/javascript";
        script.src = src;

        document.body.appendChild(script);

        script.onload = () => {
            resolve("Script loaded successfully");
        };

        script.onerror = () => {
            reject("Script loading failed");
        };
    });
};

let p5 = loadscript("https://example.com/test.js");

p5.then((value) => {
    console.log(value);
}).catch((error) => {
    console.log("Some error occurred:", error);
});
