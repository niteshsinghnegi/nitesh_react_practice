// let employee={
//     name1:"nitesh",
//     age:18,
//     domain:"python developper"
//     // run:()=>{
//     //     alert(" self run")
//     }

// console.log(employee)


// let p={
//     run:()=>{
//         alert("run")
//     }

// }

// p.__proto__={
//     name:"manyata"
// }
// employee.__proto__= p
// employee.run()

// console.log(employee.name)


// class employee{
//     constructor(givenname,domain){
//         console.log("constructer is called"+givenname+domain)
//        this.name=givenname
//        this.domain=domain
//     }
//         submit_you_resume(){
//         alert(this.name+"submit your resume  for domain"+this.domain)
//     }
//     cancel_your_aplication(){
//         alert(this.name+"cancel your apllication "+this.domain)
//     }
// }



// let Nitesh_resume1=new employee("nitesh negi","data scientest")

// let Nitesh_resume2=new employee("nitesh", "pythondeveloper")
// // Nitesh_resume2.joining("nitesh negi","data scientest")

// // Nitesh_resume1.joining("nitesh", "pythondeveloper")
// let manayta_resume=new employee("manyata","uidesigner")

// Nitesh_resume1.submit_you_resume()
// Nitesh_resume2.submit_you_resume()
// manayta_resume.submit_you_resume()
// manayta_resume.cancel_your_aplication()

// .....................script 2...................................
// class employee{
//     constructor(givenname,domain,gradutation,experice){
//         console.log("constructer is called"+givenname+ " "+domain+" " +gradutation+" "+ experice)
//        this.name=givenname
//        this.domain=domain
//        this.gradutation=gradutation
//        this.experice=experice
//     }
//     preview(){
//         alert(this.name+"submit your resume  for domain"+this.domain+"and your cousres is "+this.gradutation+"AND YOUR EXPERNICE IS "+ this.experice)
//     }
//         submit_you_resume(){
//         alert(this.name+"submit your resume  for domain"+this.domain)
//     }
//     cancel_your_aplication(){
//         alert(this.name+"cancel your apllication "+this.domain)
//     }
// }

// let emp1=new employee("nitesh","datascience","bca","fresher")
// let emp2=new employee("dinesh","data analyitcs","b.teach","fresher")
// let emp3=new employee("manayta","dataadminestrtor","bsc","experices")

// emp1.submit_you_resume()
// emp2.submit_you_resume()
// emp3.cancel_your_aplication()
// emp3.submit_you_resume()
// emp1.preview()

// ................inheritance is javascript ........................

// class Animal{
//     constructor(name,color){
//         this.name=name
//         this.color=color
//     }
//     run(){
//         console.log(this.name+"is running !")

//     }
//     shout(){
//         console.log(this.name+"is shouting")
//     }
// }
// class Monkey extends Animal{
//     eatBanana(){
//         console.log(this.name+"is eat banana")
//     }
//     hide(){
//         console.log(`${this.name} is hiding`)
//     }
// }
// let ani=new Animal("bruno","white")
// let m =new Monkey("monkey","orange")
// m.shout()
// m.eatBanana()
// ani.shout()
// m.hide()

// ..............method overrinding.................
// class Employee{
//     login(){
//         console.log(`employee has log in `)
//     }
//     logout(){
//         console.log(`employee has log out `)
//     }
//     requestleave(leave){
//         console.log(`employee has requested${leave}leave- auto appropved`)
//     }
// }

// class programmer extends Employee{
//   requestcoffie(x){
//     console.log(`employee has requested ${x} coffies`)
//   }
//     requestleave(leave){
//         // console.log(`employee has requested${leave+1} leaves (one extra leave)`)
//         super.requestleave(4)
//         console.log("one extra is granted")
//     }
// }

// // let e= new Employee()
// let e =new programmer
// e.login
// e.requestleave(3)

// ...........constructor overriding ...............//
// class Employee{
//     //  constructor(name){
//     //     console.log(name +"programmer constructor here")
//     //     this.name
//     // }
//     login(){
//         console.log(`employee has log in `)
//     }
//     logout(){
//         console.log(`employee has log out `)
//     }
//     requestleave(leave){
//         console.log(`employee has requested${leave}leave- auto appropved`)
//     }
// }


// class programmer extends Employee{
    
//      constructor(name){
//         super(name)
//         console.log(name +"programmer constructor here")
//         this.name
//     }

//     // constructor(...args){----if there is ni constructor in the chlid class ,this is creted automatically 
//     //     sueper(...args)
//     // }
//   requestcoffie(x){
//     console.log(`employee has requested ${x} coffies`)
//   }
//     requestleave(leave){
//         // console.log(`employee has requested${leave+1} leaves (one extra leave)`)
//         super.requestleave(4)
//         console.log("one extra is granted")
//     }
// }

// // let e= new Employee()
// let e =new programmer("negi")
// e.login
// e.requestleave(3)


//.......static method ...........................//
// class Student {
//     constructor(name) {
//         this.name = Student.capitalize(name);
//     }

//     attendance() {
//         console.log(this.name + " is present");
//     }

//     static capitalize(name) {
//         return name.charAt(0).toUpperCase() + name.substr(1);
//     }
// }

// let stu = new Student("nitesh");
// stu.attendance();

// getter and setter ..................

class teacher{
    constructor(name,subject){
        this._name=name
        this._subject=subject
    }

    teach(){
        console.log("Mr." + " "+this.name + " "+ "teach subject " + " " + this.subject)
    }
    get name(){
        return this._name
    }
    get subject(){
        return this._subject
    }
    set name (newname){
        this._name=newname
    }

}
let t=new teacher("nitesh")

t.teach()
console.log(t.name)
t.name="manyata"
console.log(t.name)

console.log(t instanceof teacher)