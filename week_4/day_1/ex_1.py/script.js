/*Ex 1*/

function checkDriverAge1(){

	var age = prompt("How old are you? ");

	if (Number(age) < 18) {
	alert("Sorry, you are too young to drive this car. Powering off.");
	} else if (Number(age) > 18) {
	alert("Powering on. Enjoy the ride!");
	} else if (Number(age) === 18) {
	alert("Congratulations on your first year of driving. Enjoy the ride!");
		}
}

checkDriverAge1();
checkDriverAge1();

let age=92;

function checkDriverAge(age){


	if (Number(age) < 18) {
	alert("Sorry, you are too young to drive this car. Powering off.");
	} else if (Number(age) > 18) {
	alert("Powering on. Enjoy the ride!");
	} else if (Number(age) === 18) {
	alert("Congratulations on your first year of driving. Enjoy the ride!");
		}
}

checkDriverAge(age);

/*Ex 2*/

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(){
	let item=prompt("Which item do you want?");
	let check=false;
	for (let x in amazonBasket){
		if (item===x){
			check=true;
		}
	}
	if (check){
		alert("We have your item!")
	}
	else{
		alert("We don't have your item.");
	}
}
checkBasket();


/*Ex. #3*/

var stock = { 
/*    "banana": 6, */
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

var prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

function myBill(){
	let sum=0;
	let found=false;
	for (let x in prices){
		found=false;
		for (let y in stock){
			if (x===y){
				found=true;
				break;
			}
		}
		if (found===false){
			console.log("Sorry, we don't have " + x +"s");
		}
		else if (found===true&&stock[x]>0){
			sum=sum+prices[x];
			stock[x]=stock[x]-1;
		}
		else if(stock[x]===0){
			console.log("Sorry, we're out of " + x + "s");
		}
	}
	return sum;
}

console.log("The total is: " + myBill());
console.log("Items left in stock");
for(let x in stock){
	console.log(x, stock[x]);
}


/*Ex. 4*/

function hotel_cost (nights){
	total=140*nights;
	return total;
}

function plane_ride_cost (city){
	if (city==="London"){
		return 183;
	}
	else if(city==="Paris"){
		return 220;
	}
	else{
		return 300
	}
}

console.log(hotel_cost(3));
let running=true;
let city="";
city=prompt("Which city are you visiting?")
while(running){
	if(city===null||city.length===0){
		city=prompt("Please enter a valid city.");
	}
 	else if(city.length>0 && city!=undefined){
 		running=false;
 	}
 }


console.log(plane_ride_cost(city));