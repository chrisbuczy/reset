/* multi-line
comment */

// data types: undef, null, boolean, str, int, float, obj, and symbol
var number = 5; // this is a comment
var myName = "Christian"; // var is global
let ourName = "Buczynski"; // let is within the scope of what it's in
var fullName = myName + ' ' + ourName;
const pi = 3.14;
var a; // js has undef data type

console.log(myName);
console.log(fullName);
console.log(a);

// math
console.log(1 + 1, 2 * 2, 3 - 3, 4 / 4, 5 % 2);

//increment / decrement
var myVar = 0;
myVar++;
console.log(myVar);
myVar--;
console.log(myVar);

// len
console.log(fullName.length);

// get ele at index
var Name = "Bob";
console.log(Name[0], Name[1], Name[2]);