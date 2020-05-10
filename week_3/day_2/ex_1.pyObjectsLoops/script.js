/*Ex. 1 

#1*/
let favoriteColors=["blue", "purple", "pink"];

/*#2*/
for(let i=0; i<favoriteColors.length; i++){
	num=i+1;
	console.log("My # " + num +" choice is "+favoriteColors[i]);
}

/*#3*/
for(let i=0; i<favoriteColors.length; i++){
	num=i+1;
	switch(num){
		case 1:
			console.log("My " + num +"st choice is "+favoriteColors[i]);
			break;
		case 2:
			console.log("My " + num +"nd choice is "+favoriteColors[i]);
			break;
		case 3:
			console.log("My " + num +"rd choice is "+favoriteColors[i]);
			break;
		}
	}

/*Ex. 2

#1*/
var num;
do
{
num=prompt("Enter a number:")
}
while(num<10);


/*Ex. 3

#1*/
var people = ["Greg", "Mary", "Devon", "James"];
for (let x of people){
	console.log(x);
}


/*#2*/
people.shift();
for (let x of people){
	console.log(x);
}

/*#3*/
people[2]="Jason";
for (let x of people){
	console.log(x);
}

/*#4*/
people.push("Sharon");
for (let x of people){
	console.log(x);
}

/*#5*/
for (let i=0; i<people.length; i++){
	console.log(people[i]);
	if(people[i]="Mary"){
		break;
	}

/*#6*/
}let newPeople=people.slice(1,3);
console.log("here");
for (let x of newPeople){
	console.log(x);
}

/*#7*/
console.log(people.indexOf("Mary"));

/*#8*/
console.log(people.indexOf("Foo"));

/*#9*/
let last = (people.length)-1;
console.log(last);

/*Ex. 4

#1*/
console.log("HERE!!!")
var age = [20,5,12,43,98,55];
var sum=0;

for (i=0; i<age.length; i++){
	sum = sum + age[i];
}
console.log(sum);

/*#2*/
for (i=0; i<age.length; i++){
	if (age[i]%2===0){
		console.log(age[i]);
	}
}

/*#3*/

let highest=age[0];
for(i=1; i<age.length; i++){
	if(age[i]>highest){
		highest=age[i];
	}
}
console.log("The highest number is: " + highest);


