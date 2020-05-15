/*Ex. 1
#1*/
document.getElementsByTagName("div")[0].setAttribute("id", "socialNetworkNavigation");
console.log(document.getElementsByTagName("div")[0].getAttribute("id"));

/*#2*/

let li=document.createElement("li");
let text=document.createTextNode("Logout");
li.appendChild(text);
document.body.getElementsByTagName("ul")[0].appendChild(li);


/*Bonus*/

let firstLi=document.getElementsByTagName("ul")[0].firstElementChild.textContent;
console.log(firstLi);

let lastLi=document.getElementsByTagName("ul")[0].lastElementChild.textContent;
console.log(lastLi);

