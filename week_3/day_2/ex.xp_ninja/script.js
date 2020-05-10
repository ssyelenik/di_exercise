let doubleLetter=null;
let verb="seeing";
console.log(verb.indexOf("ing"));
console.log(verb.length);
console.log(verb.length-3);
if (verb.length>=3){
	if (verb.indexOf("ing")!=verb.length-3)
	{
		doubleLetter=verb.substr(verb.length-1);
		console.log(verb+doubleLetter+"ing");
	}
	else if(verb.indexOf("ing")===verb.length-3){
	console.log(verb+"ly");
	}
}
else{
	console.log(verb);
}
