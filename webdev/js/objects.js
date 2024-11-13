var Dog = {
    "name" : "Camper",
    "legs" : 4,
    "tails" : 1,
    "friends" : ["everything"]
};

var myDog = {
    "name" : "dude",
    "legs" : 3,
    "tails" : 2,
    "friends" : []
}

// 2 different ways to print dict values
console.log(myDog["legs"]);
console.log(Dog.name);

// change dict values
myDog.name = "bob";
console.log(myDog.name);

// del ditc values
delete myDog.tails;
console.log(myDog.tails);

// check if object has property
if (myDog.hasOwnProperty("name")) {
    console.log(true);
}

else {
    console.log(false);
}

// nested objects
var myStorage = {
    "car" : {
        "inside" : {
            "glove box" : "maps",
            "passenger seat" : "crumbs"
        },
        "outside" : {
            "trunk" : [
                "groceries",
                "spare tire"
            ]
        }
    }
}

console.log(myStorage.car.inside["glove box"]);
console.log(myStorage.car.outside.trunk[0]);

// objects can also contain functions
const bicycle = {
    gear :  2,
    setGear (newGear) {
        "use strict";
        this.gear = newGear;
    }
};

bicycle.setGear(3);
console.log(bicycle.gear);


// class syntax
class spaceShuttle {
constructor(targetPlanet) {
    this.targetPlanet = targetPlanet;
    }
}
var zeus = new spaceShuttle('Jupiter');
console.log(zeus.targetPlanet);


// getters and setters
class Book {
    constructor(author) {
        this._author = author;
    }

    get writer() {
        return this._author
    }

    set writer(updatedAuthor) {
        this._author = updatedAuthor;
    }
}
var book = new Book("Christian Buczynski");
console.log(book._author);
book.writer = "J.K. Rowling";
console.log(book._author);