/*#1*/
const arr =[5,0,9,1,7,4,2,6,3,8];

let hold=0;
for (x=0; x<arr.length; x++){
	for (i=0; i<arr.length; i++){
		if (arr[i]<arr[i+1]){
			hold=arr[i];
			arr[i]=arr[i+1]
			arr[i+1]=hold;
		}
	}
}

for(let x of arr){
	console.log(x);
}

/*#2*/
let stringArr=arr.toString();
console.log(stringArr);

/*#3*/
stringArr=arr.join(" and ");
console.log(stringArr);
