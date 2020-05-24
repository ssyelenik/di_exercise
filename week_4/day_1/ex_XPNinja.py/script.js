/*Ex 1*/

function noUnique(list){
	let newlist=[];
	let hold=0;
	let duplicate=false;
	let duplicates=[];
	z=0;


	for(let x=0; x<list.length; x++){
		hold=list[x];
		duplicate=false;
		for(i=0; i<list.length; i++){
			if (hold===list[i] && x != i){
				
				
				for(let h=0; h<duplicates.length; h++){
					
					if(hold==duplicates[h]&&h>1){
						
						duplicate=true;
						break;
					}
			
				}
				duplicates.push(hold);
				z++;
			}
		
		}
		if (!duplicate){
			newlist.push(list[x]);
		}
	}


	return newlist;
}


let list=[1, 2, 3, 3, 3, 3, 4, 5];
let newlist=[];
console.log("Duplicate list");
for(i=0; i<list.length; i++){
	console.log(list[i]);
}
newlist=noUnique(list);
console.log("No duplicate list");
for(i=0; i<newlist.length; i++){
	console.log(newlist[i]);
}

/*Ex 2*/

function biggestNumberInArray(array){
	let biggestNum=0;
	let hold=0;
	for(i=0; i<array.length; i++){
		let hold=array[i];
		for (x=0; x<array.length; x++){
			if (array===undefined){
				return 0;
			}
			else if (array.length===0){
				return 0;
			}
			else if(hold===toString(hold)){
				continue;
			}
			else if(array[x]>hold){
				
				biggestNum=array[x];
			
			}
		}
	}
	
	return biggestNum;
}
let array=[-1,'a',3,100, 99, 200, 99];
let biggestNum=biggestNumberInArray(array);
console.log(biggestNum);



