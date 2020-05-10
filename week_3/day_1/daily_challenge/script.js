let str1="mix";
let str2="pod";
let hold1=str1.charAt(2);
str1=str1.replace(str1.charAt(2), str2.charAt(2));
str2=str2.replace(str2.charAt(2),hold1);
console.log(str2+" "+str1);

/* let x = prompt("Enter a Value", "0");
 let y = prompt("Enter a Value", "0");
 let num1 = parseInt(x);
 let num2 = parseInt(y);
 let sum=num1+num2;
 alert("The sum is: "+sum);*/

 var array=["Banana","Apples","Oranges","Bluberries"];
 console.log(array);
 /*Task 1*/
 array.shift();
 console.log(array);
 /*Task 2*/
 array=array.sort();
 console.log(array);
 /*Task 3*/
 array.push("Kiwi")
 console.log(array);
 /*Task 4*/
 array.splice(0,1)
 console.log(array);
 /*Task 5*/
 array.reverse();
 console.log(array);
 /*Task 5*/
 var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
 console.log(array2[3,0]);