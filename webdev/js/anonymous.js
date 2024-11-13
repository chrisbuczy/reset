// this is an anonymous function
// () specifies that it's a function
// => is the return statement
// new Date() is what it returns
magic = () => new Date();
console.log(magic());

// this is how you add parametres
var myConcat = (arr1, arr2) => arr1.concat(arr2);
console.log(myConcat([1, 2, 3], [4, 5, 6]));


const realNumbers = [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2];
const squareList = (arr) => {
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x * x);
    return squaredIntegers;
}
// in this function, filter() filters out numbers that are below 0 and decimals
// map applies x * x to each element in the list
console.log(squareList(realNumbers));

