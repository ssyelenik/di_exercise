/*Ex. 1
#1*/
document.getElementsByTagName("div")[0].style.backgroundColor="lightblue";
document.getElementsByTagName("div")[0].style.padding="50px";


/*#2*/
document.getElementsByTagName("li")[0].style.display="none";
document.getElementsByTagName("li")[1].style.border="3px solid red";

/*#3*/

document.body.style.fontSize="30px";




/*Bonus*/

if (document.getElementsByTagName("li")[0].style.display=="none"){
	alert("Hello " + document.getElementsByTagName("li")[0].textContent + " " + document.getElementsByTagName("li")[1].textContent);
}




