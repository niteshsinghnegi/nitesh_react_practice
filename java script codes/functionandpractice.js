function onePlusAvg(a,b){
    return 1+a+b/2;
}
 console.log(onePlusAvg(6,7));



 function square(a){
    return a*a;
}
 console.log(square(6));




 const multiplication=(t,u)=>{
    return t*u;
 }
console.log(multiplication(5,6));

 
// practice question
let marks = {
    negi: 67,
    suresh: 76,
    manyata: 86
};

let keys = Object.keys(marks);

for (let i = 0; i < keys.length; i++) {
    console.log("Marks of " + keys[i] + " are " + marks[keys[i]]);
}

let markss = {
    negi: 67,
    suresh: 76,
    manyata: 86
};

for (let key  in markss) {
    console.log("the marks of "+key+ "are " + markss[key]);
    console.log("Marks of " + name + " are " + markss[name]);
}

let correct_num=4;
let i 
while(i!=correct_num){
    console.log("try again ")
 i=prompt("enter the numbere ")   
}
console.log("plese enter correct numbere")
// alert("plese enter correct numbere")

const mean=(a,b,c,d)=>{
    return (a+b+c+d)/4;

}
console.log(mean(5,6,7,8))
