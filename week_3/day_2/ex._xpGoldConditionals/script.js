/*Ex:1*/

let num=prompt("Please enter a number:")
if (num%2===0){
	console.log(num + " is an even number.");
}
else{
	console.log(num + " is not an even number.")
}

/*Ex:2*/
let x=2;
let y=89;
if(x>y){
	console.log(x + " is bigger than " +y);
}
else if(y>x){
	console.log(y + " is bigger than " +x);
}
else{
	console.log(y + " and " + x + " are equal")
}

/*Ex:3*/
let language=prompt("Which language do you speak?");
switch(language){
	case "French":
		console.log("Bonjour");
		break;
	case "English":
		console.log("Hello");
		break;
	case "Hebrew":
		console.log("Shalom");
		break;
	default:
		console.log(":-)");
		break;
}

/*Ex:4*/

