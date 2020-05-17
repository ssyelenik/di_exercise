let word="";
let won=false;
let buildWord="";
let letter="";
let numTries=10;
let wrongLetters=[];
let wrongLetterIndex=0;
let allLetters=[];
let allLetterIndex=0;

function my_f(){
	/*Get the game word:*/
	while(word===""){
	word=prompt("First player: Enter the Game Word:");
	}
	word=word.toLowerCase();


	/*Show the initial setup of stars at length of word to be guessed:*/
	for (let i=0; i<word.length; i++){
		buildWord=buildWord + "*";			
	}
	console.log(buildWord);


	/*Play the game:*/
	while(numTries>0){
		getLetter();
		checkLetter();
		if(buildWord==word){
			alert("That's it. Congratulations! You won the game!");
			won=true;
			break;
		}
	

	}
	if (won===false){
		console.log("Sorry, you lost. The word is: " + word);
	}

}

function getLetter(){
	if (numTries<10){
		console.log("Here, list the wrong guesses");
		for (let x of wrongLetters){
			console.log (x + " ");
		}
	}


	let stop=false;
	let found=false;

	
	letter=prompt("Second player: Enter a letter:");	
	/*Check that the letter hasn't been guessed yet*/
	while(!stop){
		for(let x of allLetters){
			if (letter===x){
				found=true;
				break;
			}
		}
		if(found===true){
			letter=prompt("Letter invalid. Enter another guess:");
			found=false;
		}
		else{
			stop=true;
		}

	}
	
	/*Build list of guessed letters for check and display*/
	allLetters[allLetterIndex]=letter;
	allLetterIndex++;
}


function checkLetter(){
	let temp=""
	let secondCheck=-1;
	let letterFound=word.indexOf(letter);
	if(letterFound>=0){
		
		buildWord=buildWord.substr(0, letterFound) + letter + buildWord.substr(letterFound+1, word.length-letterFound-1);
		
		/*if there's double letters*/
		do{					
		temp=word.substr(letterFound+1, word.length-letterFound-1);
		secondCheck=temp.indexOf(letter);
			if (secondCheck>=0){
				letterFound=secondCheck+letterFound+1;
				buildWord=buildWord.substr(0, letterFound) + letter + buildWord.substr(letterFound+1, word.length-letterFound-1);
			}
		}
		while(secondCheck>=0);		
		console.log(buildWord);
	}
	else{
		numTries--;
		console.log("Wrong! You have " + numTries + " out of ten tries left.")
		wrongLetters[wrongLetterIndex]=letter;
		wrongLetterIndex++;
	}
}