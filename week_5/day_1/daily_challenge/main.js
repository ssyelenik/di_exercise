let featuresBtn=document.getElementById("featuresBtn");

let x=0;
featuresBtn.addEventListener("click", addItems);
featuresBtn.addEventListener("mouseover", changeColor);
featuresBtn.addEventListener("mouseout", changeBack);
featuresBtn.addEventListener("dblclick", changeNavBartextColor);
featuresBtn.addEventListener("contextmenu", changePic);

function addItems(e){
		if(x<6){
            let ul=document.createElement("ul");
    
            let li1=document.createElement("li");
            let text1 = document.createTextNode("Grade 7: Thumbs Up");

            li1.appendChild(text1);
            ul.appendChild(li1);
   
              
            
            let li2=document.createElement("li");
            let text2 = document.createTextNode("Grade 9: Just Imagine");

            li2.appendChild(text2);
            ul.appendChild(li2);
    
            document.getElementById("jumbotron").appendChild(ul);
            let newList=document.getElementsByTagName("ul")[x];
            
            newList.style.fontSize="20px";
            newList.style.margin="50px";
      		x++;
      	}

}


function changeColor(e){
	
	this.style.transition= "ease-in-out 2000ms";
	this.style.background="purple";
	this.style.width="200px";
	this.style.height="80px";
	this.style.color="yellow";
	/*e.stopPropogation();*/

}

function changeBack(e){
	this.style.transition= "ease-in-out 2000ms";
	this.style.background="none";
	this.style.width="170px";
	this.style.height="50px";
	this.style.color="white";

}

function changePic(e){

	let pic=document.getElementsByTagName("img")[0];

	if(pic.src==="file:///C:/Boot%20Camp/di_exercise/week_5/day_1/daily_challenge/dead_sea.jpg"){
		pic.src="negev.jpg";
	}
	else{
		pic.src="dead_sea.jpg";
	}

}

function changeNavBartextColor(e){
	

	let nav1=document.getElementById("nav1");
	let nav2=document.getElementById("nav2");
	let nav3=document.getElementById("nav3");
	let nav4=document.getElementById("nav4");
	let nav5=document.getElementById("nav5");


	nav1.style.color="red";
	nav2.style.color="yellow";
	nav3.style.color="green";
	nav4.style.color="blue";
	nav5.style.color="purple";

}