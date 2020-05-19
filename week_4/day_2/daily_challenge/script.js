
let allBooks=[
{
	title:"Gone With The Wind",
	author:"Margaret Mitchell",
	image:"https://i2.wp.com/8bitisland.co.nz/wp-content/uploads/2019/03/gone-with-the-wind.jpg?resize=750%2C430&ssl=1",
	alreadyRead:true
},
{
	title:"The Chosen",
	author:"Chaim Potok",
	image:"https://thechosencphs.weebly.com/uploads/2/0/4/2/20429393/6722074.jpg?442",
	alreadyRead:false
}
]


let table = document.body.firstElementChild;

/*for (i=1; i<3; i++){
	for (x=0; x<3; x++){
		for(let a in allBooks[i-1]){
			console.log(allBooks[i-1][a]);
			table.getElementsByTagName("tr")[i].getElementsByTagName("td")[x].textContent=allBooks[i-1].a;
		}
	}
}*/


table.getElementsByTagName("tr")[1].getElementsByTagName("td")[0].textContent=allBooks[0].title;
table.getElementsByTagName("tr")[1].getElementsByTagName("td")[1].textContent=allBooks[0].author;
table.getElementsByTagName("tr")[1].getElementsByTagName("td")[2].innerHTML='<img src="'+allBooks[0].image+'" width="100"/>';

table.getElementsByTagName("tr")[2].getElementsByTagName("td")[0].textContent=allBooks[1].title;
table.getElementsByTagName("tr")[2].getElementsByTagName("td")[1].textContent=allBooks[1].author;
table.getElementsByTagName("tr")[2].getElementsByTagName("td")[2].innerHTML='<img src="'+allBooks[1].image+'" width="100"/>';

if (!allBooks[0].alreadyRead){
	console.log("here");
	table.getElementsByTagName("tr")[1].style.color="red";
}

if (!allBooks[1].alreadyRead){
	console.log("here");
	table.getElementsByTagName("tr")[2].style.color="red";
}
