
const number = Math.floor(Math.random() * 20) + 1;

let guesses = 0;
let correct = false;

while (correct === false) {
const input = prompt("Enter your guess:");
const guess = Number(input);
guesses+=1;

if (guess === number) {
    correct = true;
    console.log(`Correct! You got it in ${guesses} guesses.`);

    if (guesses >= 1 && guesses <= 3) {
    console.log("Excellent!");
    } else if (guesses >= 4 && guesses <= 6) {
    console.log("Good!");
    } else {
    console.log("Needs more practice.");
    }
} else if (guess > number) {
    console.log("Too high! Try again.");
} else if (guess < number) {
    console.log("Too low! Try again.");
}
}


