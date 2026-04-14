let a = [
    "initializing hack tool",
    "connecting to facebook",
    "connecting to server 1",
    "connection failed retrying ...",
    "connecting to server 2",
    "connected successfully...",
    "username harpalyaduvanshi",
    "trying brute force",
    "200k password tried",
    "match not found",
    "another 200k password tried",
    "match not found",
    "another 200k password tried",
    "match found",
    "accessing account",
    "hack successfully"
];

// DOM element select
let Text = document.getElementById("Text");

const sleep = async (seconds) => {
    return new Promise((resolve) => {
        setTimeout(resolve, seconds * 1000);
    });
};

const showhack = async (message) => {
    await sleep(2);
    Text.innerHTML += message + "<br>";
};

(async () => {
    for (let i = 0; i < a.length; i++) {
        await showhack(a[i]);
    }
})();
