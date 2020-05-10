/*Ex:1*/
/*#1*/
let family={
	name:"Smith",
	origin:"Swiss",
	size:5
}

/*#2*/
let properties=Object.keys(family);
for(let x of properties){
	console.log(x);
}

/*#3*/
let values=Object.values(family);
for(let x of values){
	console.log(x);
}

/*Ex: 2
*/

var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

/*#1*/

console.log(building["number_levels"]);


/*#2*/

console.log(building["number_of_apt_by_level"]["1"]);
console.log(building["number_of_apt_by_level"]["3"]);

console.log(building["number_of_apt_by_level"]["3"]+building["number_of_apt_by_level"]["1"]);
/*#3*/
console.log(building["number_of_rooms_and_rent"]["Dan"][0]);

/*#4*/
if ((building["number_of_rooms_and_rent"]["Sarah"][1]+building["number_of_rooms_and_rent"]["David"][1])>building["number_of_rooms_and_rent"]["Dan"][1]){
	console.log("Dan's rent is too low!");
	building["number_of_rooms_and_rent"]["Dan"][1]=building["number_of_rooms_and_rent"]["Sarah"][1];
	console.log("Now Dan's rent is: "+building["number_of_rooms_and_rent"]["Dan"][1]);
}

/*Ex: 3*/


let personDetails = [{
  
  fullName: "John",
  mass : 60,
  height:1.66,
 BMI : function() {
    return this.mass/this.height^2;
  	}
},

{
  
  fullName: "Sally",
  mass : 50,
  height:1.69,
 BMI : function() {
    return this.mass/this.height^2;
  	}
}]
;	
console.log(personDetails[0].fullName);
console.log(personDetails[0].BMI());

if (personDetails[0].BMI()>personDetails[1].BMI())
{
	console.log(personDetails[0].fullName + " has a higher BMI.");
}
else if(personDetails[1].BMI()>personDetails[0].BMI() )
{
	console.log(personDetails[1].fullName + " has a higher BMI.");
}
else {
	console.log(personDetails[0].fullName + " and " + personDetails[1].fullName + " have the same BMI.");
}
;