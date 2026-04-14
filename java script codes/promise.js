let promise = new Promise(function (resolve, reject) {
    console.log("my brother name is abhishek ")
    resolve("manyata is my wife")
})

console.log("hello my name is nitesh")

setTimeout(() => {
    console.log("my father name is mr,khushal singh negi")
}, 2000);

console.log("my mother name is neema devi ")
console.log(promise)
