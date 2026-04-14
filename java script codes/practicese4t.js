// crate an array of numnbers and take input from user and add the array 
// let arr=[1,2,3,4,4,5,6,7,8]
// let a=prompt("enter a number")
// a=Number.parseInt(a)
// arr.push(a)
// console.log(arr)

// keep adding numbers ti the array in 1 until o is added to the array 
// let arr1=[1,2,3,4,4,5,6,7,8]
// do{
//     a=prompt("enter a number")
//     a=Number.parseInt(a)
//     arr1.push(a)
//     console.log(arr1)
// }while(a!=0)

    // filter for  number divisibke byb  by 10 form a given array 
let arry3=[1,20,24,50,5,45,60] 
let new_arry=arry3.filter((a) =>{
    return a%10==0
} )
console.log(new_arry) 

// create an arry to sqare a arry
let x=[2,3,4,5]
let squre= x.map((a)=>{
    return a*a
})
console.log(squre)


//use eto calculate an factorial of given numbere  from an array off frst n natural numbers.( n beigns the numbers whiose fact
// factrorai need  to be calculated
let x3=[2,3,4,5]
let fact= x3.reduce((a1,a2)=>{
    return a1*a2
})
console.log(fact)