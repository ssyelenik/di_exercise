    function createCalendar(elem, year, month){

		let startDay = new Date(year + "-" + month + "-01").getDay();
		// 6 - Saturday
		


		if (startDay===6){
			startDay=5;
		}
		else if(startDay===5){
			startDay=4;
		}
		else if (startDay===4){
			startDay=3;
		}
		else if(startDay===3){
			startDay=2;
		}
		else if (startDay===2){
			startDay=1;
		}
		else if(startDay===1){
			startDay=0;
		}
		else if(startDay===0){
			startDay=6;
		}

		let monthLength=daysInMonth(month, year);
		console.log(monthLength);


		for(i=0; i<startDay; i++){
		
			table.getElementsByTagName("tr")[1].children[i].textContent=".";
		}

		let firstDay=1;
		console.log(startDay);
		
		for(let x=startDay; x<7; x++){
			console.log(firstDay);
			table.getElementsByTagName("tr")[1].children[x].textContent=firstDay;
			firstDay++;
		}

		firstDayFillCalendar=8-startDay;
		for(let y=2; y<5; y++){
			for(let z=0; z<7; z++){
				table.getElementsByTagName("tr")[y].children[z].textContent=firstDayFillCalendar;
				firstDayFillCalendar++;
			}
		}

		let lastDayFillCalendar=firstDayFillCalendar;
		console.log(lastDayFillCalendar);
		let daysLeft=monthLength-lastDayFillCalendar;
		console.log(daysLeft);

		if (daysLeft<8){
			for(let h=0; h<daysLeft+1; h++){
				table.getElementsByTagName("tr")[5].children[h].textContent=lastDayFillCalendar;
				lastDayFillCalendar++;

			}
		}
		else if(daysLeft>7){
			for(let h=0; h<7; h++){
				table.getElementsByTagName("tr")[5].children[h].textContent=lastDayFillCalendar;
				lastDayFillCalendar++;
				daysLeft--;
				console.log(daysLeft);
			}
			for(let h=0; h<daysLeft+1; h++){
				table.getElementsByTagName("tr")[6].children[h].textContent=lastDayFillCalendar;
				lastDayFillCalendar++;
			}
		}

	/*	let spaces=7-daysLeft;
		for(let b=6; b>7-spaces; b--){
			table.getElementsByTagName("tr")[5].children[b].textContent=".";
		}
*/
    }


    function daysInMonth (month, year) {
    return new Date(year, month, 0).getDate();
	}




    let table = document.body.firstElementChild;
    createCalendar(table, 2015, 4);