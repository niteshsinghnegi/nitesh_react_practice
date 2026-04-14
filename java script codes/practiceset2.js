// use logical oprator  to find  whtere the age of a person  lies between 10  and 20 \
let age1= prompt("what is your agee")
if (age1>10 && age1 <20){
    console.log("your age lies between 10 and 20")
}
else {
    console.log("your age is not between 10 and 20 ")
}

// demostrate the use of switch case statemnet in js 
const a = 1
switch (a) {
    case -1 :
           console.log("it is negative numbere")
           break ;
    case 0:
        console.log("this is zero") 
        break;      
default :
        console.log ("this is a vaild number")

}

// wap in js to cheack wheter a numbere devisabel 2 or 3 
let s= prompt("what is your numbere");
r= Number.parseInt(s)
if(s%2==0 && s%3==0){
    console.log ("number divisible by 2 or 3 ")
}

let r= 12;r= Number.parseInt(s)
if(r%2==0 && r%3==0){
    console.log("number is divisible by 2 or 3");
}
else 
{
   console.log("number is  not divisible by 2 or 3") ;
}
let age = 19
let d = age>18 ? "you can drive": "you can not drive "
console.log(d)
