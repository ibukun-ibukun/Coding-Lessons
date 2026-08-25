const btn = document.querySelector("button")
const h1 = document.querySelector("h1")
const searchBox = document.getElementById("search-box")
const catFilter = document.getElementById("category-filter")
const form = document.querySelector("form")
const card = document.getElementById("inner")

function removeCard(btn){
    const card = btn.parentElement;
    card.remove()
    console.log("Item has been removed")
}

btn.addEventListener("click", () => removeCard(btn))

btn.addEventListener("click", (event) => {
    console.log(event);
    console.log(event.target)
    console.log(event.target.id)
});

searchBox.addEventListener("input", (e) => console.log(e.target.value))

catFilter.addEventListener("change", (bleh) => console.log(bleh.target.value))

form.addEventListener("submit", (e) => {
    e.preventDefault()
    console.log("form submitted!")
});

card.addEventListener("mouseover", () => {
    card.style.backgroundColor = "red";
    console.log("hovered")
});

card.addEventListener("mouseout", () => {
    card.style.backgroundColor = "blue";
    console.log("out")
});

document.addEventListener("keydown", (e) => console.log(e.key))