const person = {
    name : "chris",
    age : 16
};

// template literal with multi-line and string inerpolation
const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;
console.log(greeting);


// this is simple fields
// it makes a object and assigns each property by itself
const createPerson = (name, age, gender) => ({name, age, gender});
console.log(createPerson("Christian", 16, "male"));