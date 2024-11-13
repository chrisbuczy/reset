var x = 5;
var y = 6;

// if is t or f
function trueOrFalse(isItTrue) {
    if (isItTrue) {
        return "Yes it's true";
    }
    return "No it's false";
}

console.log(trueOrFalse(true));


if (x > y) {
    console.log("first num is bigger");
}

else if (y > x) {
    console.log("second num is bigger");
}

else {
    console.log("they are equal");
}

// difference between == and ===
// ==: finds common type between 2 vars and evaluates that
// ===: does not find common type between 2 vars and evals that
// ex. 3 == '3' | !(3 === '3')
// there is also != and !==
if (!(x === y)) {
    console.log("they are not equal");
}

// or and and examples
function andOr(ex) {
    if (ex > 25 && ex < 50) {
        console.log("ex is between 25 and 50");
    }

    if (ex == 25 || ex == 50) {
        console.log("ex equals 25 or 50");
    }
}

andOr(25)
