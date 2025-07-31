// Get user data
const userName = prompt('Your name: ');
let age = parseInt(prompt('Age: ')); // Convert from string to number
console.log('Welcome to the interactive messaging system!');
const wordsWrongs = ['Oh! some thing was wrong! please insert a valid age 😑', 'Ok bro, I think you have to insert a valid number 😐', 'Please insert a valid age 🥹'];
const dataChild = [`Hi ${userName} you are a child, keep learning and enjoying coding 😁!`, `Hi, ${userName}, you are baby 👶 but that does not mean you do not stop to learn!`, `Hi, ${userName} what are you doing here?, I bet you are eager to learn at an early age 🔥!`,` Hi, ${userName} you are a soo young, keep learning and enjoying coding 😁!`,];
const dataAdult = [`Hi ${userName} you are an adult, prepare for big opportunities in the tech enviroment 😌`, `Hi ${userName} let me know, are you here because you want a better life right? 🤑`];

// This function return random messages depending of the data
function randomWords(array) {
    let generateRandomWord = Math.floor(Math.random() * array.length);
    if (array == wordsWrongs) {
        console.error(array[generateRandomWord]);
    } else if (array == dataChild) {
        alert(array[generateRandomWord])
    } else {
        alert(array[generateRandomWord])
    }
}

// Validate and show messages
if (isNaN(age)) {
    randomWords(wordsWrongs)
} else if (age < 18) {
    randomWords(dataChild);
} else {
    randomWords(dataAdult)
}