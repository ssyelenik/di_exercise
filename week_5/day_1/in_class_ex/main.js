/*Exercise #1*/

function insert_Row(){

	let tr=document.createElement("tr");
	for(i=0; i<2; i++){
		let td=document.createElement("td");
		let text = document.createTextNode("Row3 cell1");

		td.appendChild(text);
		tr.appendChild(td);
	}
	document.body.getElementsByTagName("table")[0].appendChild(tr);

}

/*Exercise #2*/



