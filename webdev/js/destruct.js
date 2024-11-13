var voxel = {x : 3.6, y : 7.4, z : 6.54};

// this is the onger way of assigning vars to each property
var x = voxel.x;
var y = voxel.y;
var z = voxel.z;

// this is destructuring
const {x : a, y : b, z : c} = voxel;
console.log(a, b, c)

// you can also destruct nest objects
const forecast = {
    today : {min : 72, max : 83},
    tomorrow : {min : 73.3, max : 84.6},
};

const {tomorrow : {max : maxOfTomorrow}} = forecast;
console.log(maxOfTomorrow);

// you can also use this with array
const [one, two, , three] = [1, 2, 3, 4];
console.log(one, two, three);


const stats = {
    max : 56.78,
    median : 24.54,
    mode : 23.87,
    mean : 35.85,
    min : -0.75
};
const half = (function() {
    return function half({max, min}) { // this destructs it into just the max and min property
        return (max + min) / 2.0;
    };
})();
console.log(stats);
console.log(half(stats));