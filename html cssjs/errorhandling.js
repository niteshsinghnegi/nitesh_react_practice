setTimeout(() => {
    console.log("my love is .....")
}, 2000);

// try{
//   console.log(manyata)  
// }
// catch (error){
//   console.log("manyata is a girl")
// // }

// try{
//     setTimeout(() => {
//          console.log(manyata)  
//     },1000);
 
// }
// catch (error){
//   console.log("manyata is a girl")
// }
// setTimeout(() => {
//     console.log("my love is manyata")
// }, 3000);


// setTimeout(() => {
//     console.log("she is my.....")
// }, 2000);

// setTimeout(() => {
//     console.log("she is my wife ")
// }, 4000);


// custom error 

// try{
//     let number=prompt("enter your favriout number ");
//     number=Number.parseInt(number);
//     if(number!=number){
//         throw new ReferenceError("wrong input ")
//     }
// } catch(error){
//     console.log(error.name)
//     console.log(error.massage)
//     console.log(error.stack)
// }

// console.log("this is your favriout number ")


// using finaly block 
const a=()=>{


try{
    let a=prompt("enter your age")
    a=Number.parseInt(a)
    consloe.log(a)
    return
    if(a>120)
         
       throw new ReferenceError("wrong input age  ")
     
}
catch(syntax_error){
    console.log(b)

    console.log(syntax_error.name)
    console.log(syntax_error.massage)

}
finally{
    console.log("mein acha baccah hun ")
}
}
a()