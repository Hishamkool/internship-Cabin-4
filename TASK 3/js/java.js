let running =false;
let activeplayer=0;
let cs=[];
let ts=[];
const limit=20;

function GameStart(){
     var start=document.getElementById("start");
    
    if(!running){
        alert("Game has started");
        start.style.background = 'red ';
        start.value="STOP";
        running=true;
    }
    else if(running){
        alert("Game has stopped");
        start.style.background = '#33B30F';
        start.value="START"; 
        running=false;
    }

}

