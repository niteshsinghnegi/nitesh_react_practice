let p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    // resolve("value1");
  
      reject(new Error("this is an error "))
  }, 2000);
    // resolve("value1");
  
});

let p2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    // resolve("value2");
    reject(new Error("this is an error "))
  }, 2000);
});

let p3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("value3");
  }, 3000);
});

// p1.then((value) => {
//   console.log(value);
// });

// p2.then((value) => {
//   console.log(value);
// });

// p3.then((value) => {
//   console.log(value);
// });
// let promise_all = Promise.all([p1, p2, p3]);

// promise_all.then((value) => {
//     console.log(value);
// });
// let promise_all = Promise.allSettled([p1, p2, p3]);

// promise_all.then((value) => {
//     console.log(value);
// });
// let promise_all = Promise.race([p1, p2, p3]);

// promise_all.then((value) => {
//     console.log(value);
// });
// let promise_all = Promise.race([p1, p2, p3]);

// promise_all.then((value) => {
//     console.log(value);
// });
// let promise_all = Promise.any([p1, p2, p3]);

// promise_all.then((value) => {
//     console.log(value);
// });
let promise_all = Promise.resolve(9)

promise_all.then((value) => {
    console.log(value);
});
let promise_all2 = Promise.reject(new Error ("error is mine"))

promise_all2.then((value) => {
    console.log(value);
});
