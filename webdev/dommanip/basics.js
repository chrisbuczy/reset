// DOM Manipulation

// get element by id
const title = document.getElementById('main-heading');
console.log(title);

// get element by class
const listItems = document.getElementsByClassName('list-items');
console.log(listItems);

// get element by tag name
const listitems = document.getElementsByTagName('li');
console.log(listitems);

// query selector selects first item of class, id or tag
const firstList = document.querySelector('li');
console.log(firstList);

// query selector all returns node list
const container = document.querySelectorAll('div');
console.log(container);