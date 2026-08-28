const btn = document.querySelector("button")
const cart = document.getElementById("cart")
const catFilter = document.getElementById("category-filter")
const category = document.querySelector("h3")

btn.addEventListener("click", function() {
    const card = this.closest(".card");
    const image = card.querySelector("img")
    const productName = card.querySelector("h2").textContent;
    const imageSource = card.getAttribute("src")

    const cartItem = document.createElement("div")
    const cartImage = document.createElement("img")
   
})

console.log(catFilter.textContent)
console.log(category)

// catFilter.forEach("change", (e) => {
//     if (category.textContent === )
    
// })
