
  // Generate random number between 1 and 100
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const randomNumber = Math.floor(Math.random() * 10) + 1;
let attempts = 0;

console.log("🎯 Guess the number between 1 and 10");

function askQuestion() {
  rl.question("Enter your guess: ", (guess) => {
    attempts++;

    if (guess > randomNumber) {
      console.log("Too high! Try again.");
      askQuestion();
    } else if (guess < randomNumber) {
      console.log("Too low! Try again.");
      askQuestion();
    } else {
      console.log(`🎉 Correct! You guessed it in ${attempts} attempts.`);
      rl.close();
    }
  });
}

askQuestion();
