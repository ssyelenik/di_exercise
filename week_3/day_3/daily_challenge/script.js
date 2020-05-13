var word=[];
for (let i=0; i<4; i++){
	word.push(prompt("Enter a word: "));
}

for (i=0; i<word.length; i++){
	console.log(word[i]);
	console.log(typeof word[i]);
	console.log(isNaN(word[i]));
	if (isNaN(word[i])){
			}
	else{
		word.splice(i,1);
	}
}
/*let numReps=0;*/
let letterRepetition=0;
let temp="";
numReps=0;
/*let wordStatus=[];*/
let longestWord="";
for (let i=0; i<word.length; i++){	
	
	temp=word[i];
	for (let x=0; x<word[i].length; x++){
		letterRepetition=0;
		for (let z=0; z<word[i].length; z++){
			if(z===x){
				continue;
			}
			if (word[i][x]===word[i][z]){
			letterRepetition++;
			}
		}
		if (numReps<letterRepetition){
			numReps=letterRepetition;
			longestWord=word[i];
		}
	}
}
	
/*	wordStatus.splice(i,0,numReps);
}

for(let x of wordStatus){
	console.log("wordstatus" +x);
}

let hold=0
let winner=0;
for (i=0; i<wordStatus.length; i++){
	if (wordStatus[i]>hold){
		winner=i;
		hold=wordStatus[i];
	}

}*/
console.log("The word with the most repeating letters is: " + longestWord);