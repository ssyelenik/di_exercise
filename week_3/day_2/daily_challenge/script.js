let sentence="This dinner is not so positively bad!"
console.log(sentence);

let findNot=sentence.indexOf("not");
let findBad=sentence.indexOf("bad");
console.log(findNot);
console.log(findBad);

if (findBad==-1 || findNot==-1 || findNot>findBad){
	console.log(sentence);
}
else if(findNot<findBad){
	let phrase=sentence.substring(findNot,findBad+3);
	newSentence=sentence.replace(phrase,"good");
	console.log(newSentence);
}
else{
	console.log(sentence);
}
