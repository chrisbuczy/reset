var array = [];

// while loops
var i = 0;
while (i < 5) {
    array.push(i)
    i++
}

console.log(array);


// for loops
for (var i = 0; i < 5; i++) {
    array.splice(0, 1);
}
console.log(array);


// nested for loops
array.push([1, 2, 3], [4, 5, 6], [7, 8, 9]);
for (var i = 0; i < 3; i++) {
    for (var x = 0; x < 3; x++) {
        console.log(array[i][x]);
    }
}


// do while loops execute at least once every time
i = 0;
do {
    console.log(i);
}
 while (i < 0) {
    i++
 };