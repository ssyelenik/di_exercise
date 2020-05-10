var word=[];
for (let i=0; i<4; i++){
	word.push(prompt("Enter a number: "));
}

for (i=0; i<word.length; i++){
	console.log(typeof word[i]);
	if (isNaN(word[i])){
			}
	else{
		word.splice(i,1);
	}
}
let numReps=0;
let letterRepetition=0;
let wordStatus=[];
for (let i=0; i<word.length; i++){
	console.log("here: " + word[i]);	
	numReps=0;
	for (let x=0; x<word[i].length; x++){
		letterRepetition=0;
		for (let z=0; z<word[i].length; z++){
			if(z===x){
				continue;
			}
			if (word[i][x]===word[i][z]){
			letterRepetition++;
			}
		if (numReps<letterRepetition){
			numReps=letterRepetition;
		}
		}
	}
	
	wordStatus.splice(i,0,numReps);
	console.log(wordStatus[i]);
}

for(let x of wordStatus){
	console.log(x);
}
let hold=0
let winner=0;
for (i=0; i<wordStatus.length; i++){
	if (wordStatus[i]>hold){
		winner=i;
		hold=wordStatus[i];
	}

}
console.log("The word with the most repeating letters is: " +word[winner]);