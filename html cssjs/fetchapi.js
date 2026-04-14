// fetch(/1"goweather.herokuapp.com/weather/New%20York")
// .then((response)=>{
//     console.log(response.status)
//     console.log(response.ok)
//     return response.json()
// })
// .then((data)=>{
//     console.log(data)
// })
// .catch((error)=>{
//     console.log("Error:", error)
// })


// sendin post request with  fetch api 
//  const createtodo = async (todo) => {
//   let options = {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json"
//     },
//     body: JSON.stringify(todo)
//   };

//   let response = await fetch(
//     "https://jsonplaceholder.typicode.com/posts",
//     options
//   );

//   let result = await response.json();
//   return result;
// };

// const gettodo = async (id) => {
//   let response = await fetch(
//     "https://jsonplaceholder.typicode.com/posts/" + id
//   );

//   let data = await response.json();
//   return data;
// };

// const mainfunc = async () => {
//   try {
//     let todo = {
//       title: "negi",
//       body: "bhai",
//       userId: 1
//     };

//     let todor = await createtodo(todo);
//     console.log("Created Todo:", todor);

//     let fetchedTodo = await gettodo(5);
//     console.log("Fetched Todo:", fetchedTodo);

//   } catch (error) {
//     console.error("Error:", error);
//   }
// };

// mainfunc();


// .......................cookee.........................
// console.log(document.cookie)

// document.cookie = "name=nitesh99085"
// document.cookie = "name2=nit2esh99085"
// document.cookie = "name=nitesh"   // overwrite karega

// let key = prompt("enter your key")
// let value = prompt("enter your value")

// document.cookie = `${encodeURIComponent(key)}=${encodeURIComponent(value)}`

// console.log(document.cookie)

// local storage ........

// let key=prompt("enter your key ")
// let value = prompt("enter your value ")


// localStorage.setItem(key,value)
// console.log(`the value at ${key} is ${localStorage.getItem(key)}`)

// if(key == "red"|| key=="blue"){


//     localStorage.removeItem(key)

// }
// if (key==0){
//     localStorage.clear()
// }

// sesion stroage ............

// sessionStorage.getItem("name","nitesh")
// sessionStorage.clear()
// sessionStorage.removeItem("name")

// window.onstorage=(e)=>{
//     alert("change ")
//     console.log(e)
// }


// practice set ....................




