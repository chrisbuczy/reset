
function greek(val) {
    // note that cases can not be expressions like they are below
    // also note that wihtout break it will go to next case
    switch (val) {
        case 1:
            console.log("alpha");
            break;

        case 2:
            console.log("beta");
            break;

        case 3:
            console.log("gamma");
            break;

        case 4:
            console.log("sigma");
            break;
    }
}

greek(4);