/*Function:Builds list of words*/
function buildList(words){
	let temp="";
	i=0;
	running=true;
	temp=prompt("Enter a word:")
	words.push(temp);
	while(running){
		if(words[i]===null){
			alert("You're done entering words!");
			words.pop();
			running=false;
		}
		else if(words[i].length===0){
			alert("You're done entering words!");
			words.pop();
			running=false;
		}
		else if(words[i].length>0&&name!=undefined){
			i++;
			temp=prompt("Enter a word:")
			words.push(temp);
		}
	
	}
	return words;
}

/*Function:Find Longest Word*/
function findLongestWord(words){
	let longestWord=words[0];
	let longestLength=0;
	for(x=0; x<words.length; x++){
		if (words[x].length>longestLength){
			longestWord=words[x];
			longestLength=words[x].length;
		}
	}
	return longestWord;
}

/*Function:Format Stars*/
function buildStars(longestWord){
	let stars="";

	for(let i=0; i<longestWord.length+4; i++){
		stars=stars+"*";
	}
	console.log(stars);
	return stars;
}


/*Function:Print each word*/
function printWords(words, longestWord){
	let tempWord=""
	for(let z=0; z<words.length; z++){
		tempWord=buildStarsWord(words[z], longestWord.length);

	}
}


/*Function:Format each word*/
function buildStarsWord(word, longestLength){

	let difference=longestLength-word.length;
	for(i=0; i<difference+1; i++){
		word=word+ " ";
	}

	console.log("* "+word+"*");
}




/*Build list of words*/
let words=[];
buildList(words);


/*Find longest word*/
longestWord=findLongestWord(words);


/*Format*/
/*Stars*/

let stars=buildStars(longestWord);


/*Print Each Word*/
printWords(words,longestWord);




console.log(stars);