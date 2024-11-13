var myArray = ["Christian", 16]; // list
var hisArray = ["Bob", 43];
var nameArray = [myArray, hisArray]; // 2d list

console.log(nameArray);
console.log(nameArray[0][0]);

// modify array
hisArray[0] = "John";
console.log(hisArray[0]);

// append to array
nameArray.push(["Bob", 52]);
console.log(nameArray);

// add at first to array
nameArray.unshift(["Joe", 35]);
console.log(nameArray);

// remove last from array
nameArray.pop();
console.log(nameArray);

// remove first from array
nameArray.shift();
console.log(nameArray);