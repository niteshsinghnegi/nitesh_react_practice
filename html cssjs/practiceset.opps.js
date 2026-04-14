// create a java script class to create a complex number . create a constructor to set the real and complex part 
class complexNumber{
    constructor (real,imaginery){
        this._real=real
        this._imaginery=imaginery

    }

add ( number ){
    this.real= this.real+ number.real
    this.imaginery= this.imaginery+ number.imaginery
   
}
get real(){
    return this._real

}
get imaginery(){
    return this._imaginery

}
set imaginery(newimaginery){
    this._imaginery=newimaginery

}
set real(newreal){
    this._real=newreal

}

}

let num1= new  complexNumber(4,2)
console.log(num1.real,num1.imaginery)
num1.real=2
num1.imaginery=6
let num2= new complexNumber(7,6)
 num1.add(num2)
console.log(`${num1.real}+  ${num1.imaginery} i `)

// create a classstudent from a human aclass override a method & see changes

class human {
    constructor (name ,favfood){
    this.name=name
    this.favfood=favfood
    }
    speak(){
     console.log(this.name +"human  is speaking  ")
    }
}

class student extends human {

    speak(){
        console.log(this.name + "student is speaking ")
    }
}

let stu = new student ("Nitesh","biryani ")
stu.speak()

console.log( student instanceof human)