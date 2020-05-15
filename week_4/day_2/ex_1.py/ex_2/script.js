/*Ex. 2
#1*/
document.getElementsByTagName("li")[1].textContent="Richard";

/*#2*/

let ul=document.getElementsByTagName("ul");
for (x of ul){
	x.children[0].textContent="Sharon";
}

/*#3*/

let para=document.createElement("p");
let text=document.createTextNode("Hey students");
para.appendChild(text);

let ul1=document.getElementsByTagName("ul")[1];
document.body.insertBefore(para, ul1);

let para1=document.createElement("p");
let text1=document.createTextNode("Hey students");
para1.appendChild(text1);
document.body.appendChild(para1);

/*#4*/
let parentElem=document.getElementsByTagName("ul")[1];
let childElem=document.getElementsByTagName("li")[3];

parentElem.removeChild(childElem);

/*#5*/
let allUl=document.getElementsByTagName("ul");
for (let i=0; i<allUl.length; i++){
document.getElementsByTagName("ul")[i].setAttribute("class", "student_list");
console.log(document.getElementsByTagName("ul")[i].getAttribute("class"));
}

document.getElementsByTagName("ul")[0].classList.add("university");
console.log(document.getElementsByTagName("ul")[0].getAttribute("class"));



/*
let firstLi=document.getElementsByTagName("ul")[0].firstElementChild.textContent;
console.log(firstLi);

let lastLi=document.getElementsByTagName("ul")[0].lastElementChild.textContent;
console.log(lastLi);*/

/*Bonus*/