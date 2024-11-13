// Event listener
// element.addEventListener("click", function);
const button2 = document.querySelector(".btn-2");
const main = document.querySelector("body");
var count = 0;
var transOrColor = 0;

function addele() {
    if (count < 4) {
        const para = document.createElement("p");
        main.append(para);
        if (count < 3) {
            para.innerText = "you just clicked me";
        }
        else {
            para.innerText = "this was the last time to click me";
        }
    }
    count++;

}


button2.addEventListener("click", addele);


const boxColor = document.querySelector(".box3");

function changeBgColor() {
    transOrColor+=1;
    if (transOrColor % 2 == 0) {
        boxColor.style.backgroundColor = "blue";
    }

    else {
        boxColor.style.backgroundColor = "white";
    }
}

boxColor.addEventListener("mouseover", changeBgColor);



