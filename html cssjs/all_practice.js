// let a = "nitesh singh negi ";
// console.log(a)

// object creation 
// const student_name ={
//     name:"nitesh singh negi ",
//     age:19,
//     marks: 670,
//     religion:"hindu"

// }
// console.log(student_name);
// console.log(student_name["name"])

// let a= prompt("what is your name ");
// if(a=="manyata"){
//     alert("i love you manyata ")
// }
// else {
//     alert("who are you ?")
// }

// let person = prompt("what is your name ");
// console.log(person)
// alert(person)
// let person_age = prompt("what is your age");
// person_age = Number.parseInt(person_age);
// console.log(person_age);
// alert(person_age)

// if (person_age < 0) {
//     console.log("it is vaild age")
// }
// else if (person_age > 9) {
//     console.log("you are kid , you can not drive this time")
// }
// else if (person_age < 18 && person_age >= 19) {
//     console.log("your are drive now")
//     alert("ab tum drive kar skte ho")
// }
// else {
//     console.log("given age is invaild")
// }

// let start_limt = 10;
// while (start_limt<=10){
//     console.log("*")

// }


// for ( i =0;i<10 ;i++){
//     console.log(i)
// }

// let num = 1 ;
// do {
//     console.log("numbers", i );
//     i++;
// }while(i<=5);

// const software_enginear={
//     name:"nitesh negi ",
//     pakage: "12 LPA",
//     role: "software developer",
//     company :"google"
// }
// for (let key in software_enginear){
//     console.log(key+ ":" , software_enginear[key])
// }

// let arr1=[1,2,3,4]
// for (let value of arr1){
//     console.log(value )
// }

// let arr2=[1,23,4];
// arr2.forEach(function(value2){
//     console.log(value2)
// }
// );

const sum =(p,q)=>{
    return p+q;
}

let a= 12;
let b = 12;
let result=sum(a,b);

console.log(result);

function multiplication(a1,b1){
    return a1*b1
}

let s1=3;
let s2=2;
let result2= multiplication(s1,s2)

console.log(result2);


const linearsearch=(arr21,n,target1)=>{
    for (let i = 0 ; i<n ; i++){
        if(arr21[i]==target1){
  return i;
        }
    }
       return -1; 
    }

arr2=[1,2,3];
n=3;
target=3;
let linear_serach_answer=linearsearch(arr2,target,n);
console.log(linear_serach_answer);

let namer= "negi ";
console.log(namer.length)

let sentence=`i love"negi"`;
console.log(sentence)

let pati= "nitesh singh negi ";
let patni = "manyata";


let love= `${pati}is husband of a ${patni}`;
console.log(love)

let string ="nitesh"
console.log(string.length)
console.log(string.toUpperCase())
console.log(string.trim())
console.log(string.replace("negi"))
console.log(string.concat("negi"))
console.log(string.slice(2,3))
