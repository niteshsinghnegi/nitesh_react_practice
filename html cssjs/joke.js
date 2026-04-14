let jokeBox = document.getElementById("jokeBox");

// Fetch jokes from internet
fetch("https://official-joke-api.appspot.com/jokes/programming/ten")
.then(response => response.json())
.then(jokesArray => {

    // Minimum length check (10 jokes)
    if (jokesArray.length >= 10) {

        // Random index using Math.random()
        let randomIndex = Math.floor(Math.random() * jokesArray.length);

        // Show random joke using innerHTML
        jokeBox.innerHTML =
            jokesArray[randomIndex].setup +
            "<br><br><b>" +
            jokesArray[randomIndex].punchline +
            "</b>";
    }
})
.catch(error => {
    jokeBox.innerHTML = "Failed to load joke 😢";
});
