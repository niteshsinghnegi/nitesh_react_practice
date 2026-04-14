// const loadscript = (src) => {
//     return new Promise((resolve, reject) => {
//         let script = document.createElement("script");
//         script.src = src;

//         script.onload = () => {
//             resolve("Script loaded successfully");
//         };

//         script.onerror = () => {
//             reject("Script load failed");
//         };

//         document.head.appendChild(script);
//     });
// };

//   let a =  loadscript("https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js")
//  a.then((value)  =>{
//     console.log(value)
//  })           
 // const main1 = async () => {
//     try {
//         let a = await loadscript(
//             "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js"
//         );
//         console.log(a);
//         console.log(_.chunk([1,2,3,4], 2)); // lodash test
//     } catch (err) {
//         console.log(err);
//     }
// };

// main1()


// let p = () => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             reject(new Error("it is not acceptable"));
//         }, 3000);
//     });
// };

// let a = async () => {
//     try {
//         let c = await p();
//         console.log(c);
//     } catch (err) {
//         console.log("this error has been handled");
//         console.log(err.message);
//     }
// };

// a();

let p1 = async () => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(10);
        }, 3000);
    });
};

let p2 = async () => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(20);
        }, 1000);
    });
};

let p3 = async () => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(30);
        }, 2000);
    });
};

const run = async () => {
    console.time("run");

    // let a1 = await p1(); // 3 sec
    // let a2 = await p2(); // 1 sec
    // let a3 = await p3(); // 2 sec

    // console.log(a1, a2, a3);
     let a1 =  p1(); // 3 sec
    let a2 =  p2(); // 1 sec
    let a3 =  p3(); // 2 sec
    let a1a2a3= await Promise.all[a1,a2,a3]
    console.log(a1a2a3)



    console.timeEnd("run"); 
};

run();
