let running =false;
let activeplayer=0;
let cs=[];
let ts=[];
const limit=20;
var flag=0;

function GameStart(){
     var start=document.getElementById("start");
    
    if(!running){
        flag=1;
        
        // alert("Game has started");
        start.style.background = 'red ';
        start.value="STOP";
        document.getElementById("boxone").style.boxShadow="0px 0px  30px 15px lightgreen";
        running=true;
    }
    else if(running){
        flag=0;
        // alert("Game has stopped");
        start.style.background = '#33B30F';
        start.value="START"; 
        document.getElementById("boxone").style.boxShadow="";
        document.getElementById("boxtwo").style.boxShadow="";
        running=false;
    }
    if(flag==0){
        document.getElementById("Face").src="images/Red-Dice-PNG-Transparent-File.png"
    }

}
function rollOne(){
    if(flag==1){
        var df=document.getElementById("Face");
        df.style.color= 'white';
        var no=Math.floor((Math.random() *6) +1);
        
        // document.getElementById("boxone").style.boxShadow="0px 0px  30px 15px lightgreen";
        if(no==1){
        document.getElementById("Face").src="images/1.png";
        }
        if(no==2){
            document.getElementById("Face").src="images/2.png";
        }
        if(no==3){
            document.getElementById("Face").src="images/3.png";
        }
        if(no==4){
            document.getElementById("Face").src="images/4.png";
        }
        if(no==5){
            document.getElementById("Face").src="images/5.png";
        }
        if(no==6){
            document.getElementById("Face").src="images/6.png";
        }
       

    }
    
}
