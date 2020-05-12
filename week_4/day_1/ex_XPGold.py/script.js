function playTheGame(play){
	
	if (play){
		let number=prompt("Enter a number between 1 and 10");
		if (number.length===0){
			alert("Sorry it's not a good number, Goodbye");
			throw new Error('This is not an error. This is just to abort javascript');
		}
		else if(number < 0 || number > 10){
			alert("Sorry it's not a good number, Goodbye");
			throw new Error('This is not an error. This is just to abort javascript');
		}
		else{
			alert("Let's see if you guessed the number!")
			return parseInt(number);
		}
	}
	else{
		alert("No problem, Goodbye");
		throw new Error('This is not an error. This is just to abort javascript');
	}
}


const randomize = () => Math.floor(Math.random() * 10) + 1;

function test(myNumber, computerNumber, i){


	if(myNumber===computerNumber){
		alert("Congratulations! You won!");
		let result=true;
		return result;
	}
	else if(myNumber>computerNumber&&i<3){
		alert("Your number is too big. Guess again!")
		let result=false;
		return result;
	}
	else if(myNumber<computerNumber&&i<3){
		alert("Your number is too small. Guess again!")
		let result=false;
		return result;
	}
	else if(myNumber!=computerNumber&&i===3)
		alert("That was your last guess. The random number was " +computerNumber);
}

function nextChances(result){
	for (i=0; i<4; i++){
		result=test(myNumber, computerNumber, i);
		if (result){
			break;
		}
		else if (!result && i<3){
			play=confirm("Do you want to guess again?");
			myNumber=playTheGame(play);
		}
	}
}

let play=confirm("Do you want to play the game?");
let myNumber=playTheGame(play);
let computerNumber=randomize();

let result=false;
nextChances(result);


