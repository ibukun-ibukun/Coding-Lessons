
// // array.method(function(item) => {
// // })
// // array.method(item => {
// // })
// // array.method((item, index) => {
// // })
// /* 
// const toys = ["Toy Cars", "Teddy Bear", "Building Block"]

// toys.forEach(toy => {
//     console.log(toy)
// });

// toys.forEach((toy, index) => {
//     console.log(`${index + 1}.  ${toy}`)
// });
//  */

 const products2 = [
    {id:1, name: "Toy Cars",categories: "Vehicles"},
    {id:2, name: "Teddy Bear", categories: "Soft Toys" },
    {id:3, name: "Building Blocks", categories: "Plastics"},
    {id:4, name: "Toy Trucks", categories: "Vehicles"}
 ]
// let total = 0;

// products.forEach(product => {
//     console.log(`${product.name} -> ${product.price}`)
//     total += product.price;
// });

//console.log(total);

const prices = [7000, 1000, 350, 50, 1230, 8000, 6780, 1650, 11000];
const discountedPrice = prices.map(price => price * 0.9);

console.log(discountedPrice);

const formatted = prices.map(price => `${price.toLocaleString("en-NG",{
    style: "currency",
    currency: "NGN"
})}`)
console.log(formatted)

//const productCard = products.map(product => `<div class='card'>
//<h3>${product.name}</h3>
//<p>N${product.price}</p></div>`
//)

//console.log(productCard);

const affordable = prices.filter(price => price <= 5000)
console.log(affordable)

const vehicles = products2.filter(p => p.categories === "Vehicles")
console.log(vehicles)

const found = products2. find(p => p.id === 2)
console.log(found)

const hasExpensivePrices = prices.some(p => p >= 10000)
console.log(hasExpensivePrices)

Array.reduce((acumulator, currentItem) => {
    return acumulator + currentItem;
}, startingValue);

const total = prices.reduce((sum, price) => {
    return sum + price
}, 0)

console.log(total)

const lowPrice = products2
                        .filter(p => p.price <= 6000)
                        .map(p => `${p.name} - ${p.price}`)


console.log(lowPrice)
lowPrice.forEach(item => console.log(item))                        


