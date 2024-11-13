// let variables cannot be assigned in the same scope more than once
// let name = "Christian";
// let name = "Buczynski"; 
// this would give an error
// const can't be changed
var x = 5;
var x = 1;
const pi = 3.14159;
console.log(x);

// const arrays can still be mutated
// same with objects
const s = [5, 7, 2];
s[0] = "const list has been changed";
console.log(s);


