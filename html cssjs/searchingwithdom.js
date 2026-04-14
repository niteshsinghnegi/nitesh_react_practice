// function liveSearch() {
//     let input = document.getElementById("searchInput").value.toLowerCase();
//     let cards = document.getElementsByClassName("cricketer");

//     for (let i = 0; i < cards.length; i++) {
//         let name = cards[i]
//                     .getElementsByClassName("name")[0]
//                     .innerText
//                     .toLowerCase();

//         if (name.includes(input)) {
//             cards[i].style.display = "block";
//         } else {
//             cards[i].style.display = "none";
//         }
//     }
// }

// function filterCountry() {
//     let filter = document.getElementById("countryFilter").value;
//     let cards = document.getElementsByClassName("cricketer");

//     for (let i = 0; i < cards.length; i++) {

//         if (filter === "all") {
//             cards[i].style.display = "block";
//         } 
//         else if (cards[i].classList.contains(filter)) {
//             cards[i].style.display = "block";
//         } 
//         else {
//             cards[i].style.display = "none";
//         }
//     }
// }



