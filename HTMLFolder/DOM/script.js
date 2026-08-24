//const title = document.getElementById("title")

const title = document.querySelector("#title")
const allCards = document.querySelectorAll(".card")
const pTag = document.querySelector(".changes")
const changeToDiv = document.getElementById("inner")
const body = document.querySelector("body")
const h1 = document.querySelector("h1")
const lastItem  = document.querySelector("#last-item")

pTag.textContent = "Wow I changed";
console.log(pTag)


console.log(changeToDiv)
changeToDiv.innerHTML = "<div><strong>Bold</strong></div>"
console.log(title)
console.log(allCards)
allCards.forEach(card => console.log(card.textContent))

pTag.style.color = "blue";
pTag.style.fontSize = "45px"
body.style.backgroundColor = "black";
body.style.color = "white";

// allCards.classList.add("highlighted")

h1.setAttribute("class", "hero section")

const newCard = document.createElement("div")
newCard.textContent = "Toy Car - 5400";
newCard.classList.add("cart-item");
lastItem.appendChild(newCard);

function addItemtoCart(itemName, itemPrice) {
    const item = document.createElement("li")
    const wordList = document.getElementById("card-list")

    item.textContent = `${itemName} - ₦${itemPrice}`
    wordList.appendChild(item)
}

addItemtoCart("Toy-Car", "80000")
addItemtoCart("Doll", "56000")
addItemtoCart("Blocks", "45000")

h1.remove()

function removeCard(btn){
    const card = btn.parentElement;
    card.remove()
}