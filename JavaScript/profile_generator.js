
const myAge = 20;

const friend1Name = "Chidinma";
const friend1Age = 22;
const friend1City = "Port Harcourt";
const friend1FunFact = "She can solve a Rubik's cube in under a minute.";

console.log(`
===================
${friend1Name}'s Profile
===================
Age: ${friend1Age}
City: ${friend1City}
Fun Fact: ${friend1FunFact}
===================
`);

console.log(friend1Name.toUpperCase());
console.log(`${friend1Name}'s name has ${friend1Name.length} characters.`);

if (friend1Age > myAge) {
  console.log(`${friend1Name} is older than you.`);
} else if (friend1Age < myAge) {
  console.log(`${friend1Name} is younger than you.`);
} else {
  console.log(`${friend1Name} is the same age as you.`);
}

const friend2Name = "Tobenna";
const friend2Age = 19;
const friend2City = "Lagos";
const friend2FunFact = "He has watched every Marvel movie in release order twice.";

console.log(`
===================
${friend2Name}'s Profile
===================
Age: ${friend2Age}
City: ${friend2City}
Fun Fact: ${friend2FunFact}
===================
`);

console.log(friend2Name.toUpperCase());
console.log(`${friend2Name}'s name has ${friend2Name.length} characters.`);

if (friend2Age > myAge) {
  console.log(`${friend2Name} is older than you.`);
} else if (friend2Age < myAge) {
  console.log(`${friend2Name} is younger than you.`);
} else {
  console.log(`${friend2Name} is the same age as you.`);
}

const friend3Name = "Amarachi";
const friend3Age = 20;
const friend3City = "Owerri";
const friend3FunFact = "She has never lost a game of Scrabble.";

console.log(`
===================
${friend3Name}'s Profile
===================
Age: ${friend3Age}
City: ${friend3City}
Fun Fact: ${friend3FunFact}
===================
`);

console.log(friend3Name.toUpperCase());
console.log(`${friend3Name}'s name has ${friend3Name.length} characters.`);

if (friend3Age > myAge) {
  console.log(`${friend3Name} is older than you.`);
} else if (friend3Age < myAge) {
  console.log(`${friend3Name} is younger than you.`);
} else {
  console.log(`${friend3Name} is the same age as you.`);
}

let friendCount = 0;
friendCount = friendCount + 1;
friendCount = friendCount + 1;
friendCount = friendCount + 1;

console.log(`You have ${friendCount} amazing friends!`);
