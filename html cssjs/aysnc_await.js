 async function negi(){

        let bareillyweather= new Promise((resolve,reject)=>{
         setTimeout(() => {
        resolve("bareilly temprature is 20 deg")
    }, 2000);
});

let delhiweather= new Promise((resolve,reject)=>{
    setTimeout(() => {
        resolve("delhi temprature is 25 deg")
    }, 4000);
});
// bareillyweather.then(alert)
//  delhiweather.then(alert)
console.log("fetching bareilly weather please wait .....")
let bareillyweatherw= await bareillyweather
console.log("the bareilly weather has been fatched "+bareillyweatherw)

console.log("fetching bareilly weather")
 let delhiweatherw= await delhiweather
 console.log("the delhi weather is also feched"+delhiweatherw)
 return [bareillyweatherw,delhiweatherw]
}

const sigmanegi=async()=>{
    console.log("nitesh negi is  sigma boy ")
}
const main1= async()=>{


console.log("welcome to wearther control room ")
let nitesh= await negi()
let singh = await sigmanegi()


}
main1()
