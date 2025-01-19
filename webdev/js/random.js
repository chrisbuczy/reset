// random num between 0 and 19
function randomFraction() {
    return Math.floor(Math.random() * 20);
}

console.log(randomFraction());


function randomRange(ourMin, ourMax) {
    return Math.floor(Math.random() * (ourMax - ourMin + 1)) + ourMin;
}

console.log(randomRange(0, 20));