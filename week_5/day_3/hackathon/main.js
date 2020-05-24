/*let firstPage=document.getElementsByClassName("container")[0];*/
let firstPage=document.getElementsByTagName("div")[0];
firstPage.scrollIntoView();

let name="";
let submitInfo=document.getElementsByTagName("button")[0];
submitInfo.addEventListener("click", startTest);


document.body.classList.add("stop-scrolling");



let button=document.getElementsByTagName("button")[1];
button.addEventListener("click", done);


    function startTest(){

        name=document.getElementById("name").value;
        let email=document.getElementById("email").value;

        let checkPeriod=email.indexOf(".");
        let checkAmerpsand=email.indexOf("@");

        if (checkPeriod===-1 || checkAmerpsand===-1 || checkPeriod===0 || checkAmerpsand===0 || checkPeriod===email.length-1 || checkAmerpsand===email.length-1 || checkAmerpsand===checkPeriod+1 || checkPeriod===checkAmerpsand+1){
            alert("Invalid e-mail address. Please re-enter.");

        }
        else{
          document.body.classList.remove("stop-scrolling");
          let question2=document.getElementsByClassName("questionsGroup")[0];
          question2.scrollIntoView();

        }
        

    }

function done(element){
  element.preventDefault();
  let questionValueArr=[];
  let temp=0;
  let id="myRange";
  let questionElementArr=document.getElementsByTagName("question");
  


  for (let i=0; i<14; i++){
    let qNum=i+1;

    id="myRange"+qNum;

    temp=document.getElementById(id).value;
    if(temp>0 && temp<20){
        temp=1;
    }
    else if(temp>19 && temp<40){
        temp=2;
    }
    else if(temp>39 && temp<60){
        temp=3;
    }
    else if(temp>59 && temp<80){
        temp=4;
    }
    else if(temp>79 && temp<101){
        temp=5;
    }

    questionValueArr.push(temp);

  }
  

  let Q15=document.forms[0].Q15.value;
  if(Q15=="1" || Q15=="2" || Q15=="3" || Q15=="4" || Q15=="5"){
    questionValueArr.push(parseInt(Q15));
  }
  else{
    alert("Please select an answer for Question 15!");
  }

  let Q16=document.forms[0].Q16.value;
  if(Q16=="1" || Q16=="2" || Q16=="3" || Q16=="4" || Q16=="5"){
    questionValueArr.push(parseInt(Q16));
  }
  else{
    alert("Please select an answer for Question 16!");
  }


  let Q17=document.forms[0].Q17.value;
  if(Q17=="1" || Q17=="2" || Q17=="3" || Q17=="4" || Q17=="5"){
    questionValueArr.push(parseInt(Q17));
  }
  else{
    alert("Please select an answer for Question 17!");
  }

  let Q18=document.forms[0].Q18.value;
  if(Q18=="1" || Q18=="2" || Q18=="3" || Q18=="4" || Q18=="5"){
    questionValueArr.push(parseInt(Q18));
  }
  else{
    alert("Please select an answer for Question 18!");
  }

  let Q19=document.forms[0].Q19.value;
  if(Q19=="1" || Q19=="2" || Q19=="3" || Q19=="4" || Q19=="5"){
    questionValueArr.push(parseInt(Q19));
  }
  else{
    alert("Please select an answer for Question 19!");
  }

  let Q20=document.forms[0].Q20.value;
  if(Q20=="1" || Q20=="2" || Q20=="3" || Q20=="4" || Q20=="5"){
    questionValueArr.push(parseInt(Q20));
  }
  else{
    alert("Please select an answer for Question 20!");
  }

  
  let result=getResult(questionValueArr);

  display(result);

}


function getResult(v){
/*  for(let i=0; i<20; i++){
    console.log(v[i]);
  }*/
  console.log("V " + v[0] + v[1]);
  let A=v[0]+v[1]+v[2]+v[4]+v[7]+v[9]+v[10]+v[11]+v[13]+v[17]+v[19];
  let B=v[3]+v[5]+v[6]+v[8]+v[12]+v[14]+v[15]+v[16]+v[18];
  let X=66-A+B;
  console.log("x " + X);
  let result="";
  if(X>19 && X<56){
     result="leftBrained";
    }
  else if(X>55 && X<65){
      result="noBrained";
    }
  else if(X>64 && X<101){
      result="rightBrained";
  }
  return result;

}

function display(result){
    let div=document.createElement("div");
    div.className="space";
    document.getElementsByClassName("questionsGroup")[0].appendChild(div);

  let greyArea=document.getElementsByClassName("questionsGroup")[0];
  greyArea.style.height="8000px";
  if (result=="leftBrained"){
    let message=name + ", you are left-brained!"
    let h1=document.createElement("h1");
    h1.className="finalMsgH";
    let text=document.createTextNode(message);
    h1.appendChild(text);
    document.getElementsByClassName("space")[0].appendChild(h1);
     

    let h2=document.createElement("h2");
    h2.className="finalMsgT";
    let text2=document.createTextNode("You are verbal, analytical, and orderly. You have a digital way of thinking. You're better at things like reading, writing, and computations. Your strong suits are: logic, sequencing, linear thinking, mathematics, facts, and thinking in words.");
    h2.appendChild(text2);
    document.getElementsByClassName("space")[0].appendChild(h2);
  }
  else if (result=="rightBrained"){
    let message=name + ", you are right-brained!"
    let h1=document.createElement("h1");
    h1.className="finalMsgH";
    let text=document.createTextNode(message);
    h1.appendChild(text);
    document.getElementsByClassName("space")[0].appendChild(h1);
     

    let h2=document.createElement("h2");
    h2.className="finalMsgT";
    let text2=document.createTextNode("You are visual and intuitive. You have an analog way of thinking. You are more creative and less organized. You are imaginative. You think holistically and intuitively. You are interested in the arts and have a great sense of rhythm. You pick up on non-verbal cues, are in touch with your feelings, and like to daydream.");
    h2.appendChild(text2);
    document.getElementsByClassName("space")[0].appendChild(h2);
 
  }

  else if (result=="noBrained"){
    let message=name + ", you are neither left-brained nor right-brained!"
    let h1=document.createElement("h1");
    h1.className="finalMsgH";
    let text=document.createTextNode(message);
    h1.appendChild(text);
    document.getElementsByClassName("space")[0].appendChild(h1);
     

    let h2=document.createElement("h2");
    h2.className="finalMsgT";
    let text2=document.createTextNode("You are verbal, analytical, and orderly. You are also visual and intuitive. You're good at things like reading, writing, and computations, and you are creative at the same time. Your strong suits are: logic, sequencing, linear thinking, mathematics, facts, thinking in words, as well as beign imaginative, intuitive, and in touch with your feelings. You can also picking up on on-verbal and are artistic.");
    h2.appendChild(text2);
    document.getElementsByClassName("space")[0].appendChild(h2);

  }

    let a=document.createElement("a");
    a.setAttribute("href", "index1.html");
    a.className="finalMsgL";
    let text3=document.createTextNode("Click here to take the test again");
    a.appendChild(text3);
    document.getElementsByClassName("space")[0].appendChild(a);

  finalMsg=document.getElementsByClassName("questionsGroup")[0].lastElementChild;
  finalMsg.scrollIntoView();  
  document.body.classList.add("stop-scrolling");
}