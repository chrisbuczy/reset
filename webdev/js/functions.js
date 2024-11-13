// define function
function print(something) {
    return something;
}

// function call
console.log(print("hello world"))


function nextInLine(arr, item) {
    arr.push(item)
    return item;
}

var testArr = [1, 2, 3, 4, 5];

// json.stringify changes list to string for print statement
console.log("Before: " + JSON.stringify(testArr)); 
console.log(nextInLine(testArr, 6));
console.log("After: " + JSON.stringify(testArr));





