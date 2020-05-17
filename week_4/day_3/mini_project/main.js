let num1="";
let num2="";
let onNum1=true;
let decimal=false;
let op="";
function my_f(arg){

	let displayBox=document.getElementsByTagName("div")[2];


	if (!isNaN(arg)){
		if(onNum1){
			num1=num1+arg;
			displayBox.textContent=num1;
		}
		else{
			num2=num2+arg;
			displayBox.textContent=num2;
		}
	}

	else if(arg==="."){

		if (!decimal){

			if(onNum1){
				num1=num1+arg;
				displayBox.textContent=num1;
			}
			else{
				num2=num2+arg;
				displayBox.textContent=num2;
			}
		}
		decimal=true;
	}



	else if(arg==="+" || arg==="*" || arg==="-" || arg==="/"){			
			op=arg;
			onNum1=false;
			decimal=false;
	}

	else if(arg==="=" && num1!="" && num2!=""){
		calculate(parseFloat(num1), parseFloat(num2), op);
		num1="";
		num2="";
		onNum1=true;
		op=""
		decimal=false;
	}

	else if(arg==="reset"){
		displayBox.textContent="0";
		num1="";
		num2="";
		onNum1=true;
		op=""
		decimal=false;
	}

	else if(arg==="clear"){
		if(num1!="" && op!="" && num2!=""){
			num2="";
			displayBox.textContent="";
			decimal=false;
		}
		else if(num1!="" && op!="" && num2==""){
			op="";
		}
		else if(num1!="" && op=="" && num2==""){
			num1="";
			displayBox.textContent="";
			decimal=false;
		}
		else{
			displayBox.textContent="";
		}
	}


}


function calculate(num1, num2, op){
	let answer=0;
	console.log("here");
	switch(op) {
	  case "+":
	    answer=num1 + num2;
	    break;
	  case "-":
	    answer=num1 - num2;
	    break;
	  case "*":
	    answer=num1 * num2;
	    break;
	  case "/":
	  	if(num2>0){
		    answer=num1 / num2;
		    break;
		}
	}
 	document.getElementsByTagName("div")[2].innerHTML=answer;
}