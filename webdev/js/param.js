// you can specify values of parametres
function increment(numb, value=1) {
    return numb += value;
}
console.log(increment(5));


// rest operator
// ...args puts every given parametre into a single array
const sum = (function() {
    return function sum(...args) {
        return args.reduce((a, b) => a + b, 0);
    }
})();
console.log(sum(1, 2, 3, 4));


// spread operator
const arr1 = ['Jan', 'Feb', 'Mar', 'Apr', 'May'];
let arr2;
(function() {
    arr2 = [...arr1]; // try switch it to arr2 = arr1 and see what it prints
    arr1[0] = 'potato';
})();
console.log(arr2)


// note that ...arr is also the var name
const source = [1, 2, 3, 4, 5];
function removeFirstTwo(list) {
    const [ , , ...arr] = list;
    return arr;
}
const arr = removeFirstTwo(source);
console.log(arr);
console.log(source);