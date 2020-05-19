    function calculateTip(){
        let billAmt=document.getElementsByTagName("input")[0].value;
        let serviceQual=document.getElementsByTagName("select")[0].value;
        let numOfPeople=document.getElementsByTagName("input")[1].value;



        if(serviceQual==0 || billAmt=="" || billAmt==0){
            alert("You entered an invalid amount. Please re-enter the bill amount or service quality.");
        }

        if(numOfPeople=="" || numOfPeople<1){
            numOfPeople=1;
        }


        let total=billAmt*serviceQual;
        total=total.toFixed(2);


        let totalEach=total/numOfPeople;
        totalEach=totalEach.toFixed(2);


        let totalDisplay=document.getElementsByTagName("span")[0];
        totalDisplay.textContent="The Tip Came Out To: " + total ;
        totalDisplay.style.marginRight="20px";

        let totalEachDisplay=document.getElementsByTagName("small")[0];
        totalEachDisplay.textContent="You Each Have To Pay: " + totalEach;

    }


    function checkEmail(){


        let email=document.getElementById("email").value;

        let checkPeriod=email.indexOf(".");
        let checkAmerpsand=email.indexOf("@");

        if (checkPeriod===-1 || checkAmerpsand===-1 || checkPeriod===0 || checkAmerpsand===0 || checkPeriod===email.length-1 || checkAmerpsand===email.length-1 || checkAmerpsand===checkPeriod+1 || checkPeriod===checkAmerpsand+1){
            alert("Invalid e-mail address. Please re-enter.");

        }

    }

    let calculateBtn=document.getElementsByTagName("button")[0];
    calculateBtn.addEventListener("click", calculateTip);

    let emailBtn=document.getElementById("submitEmail");
    emailBtn.addEventListener("click", checkEmail);
