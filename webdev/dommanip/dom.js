// DOM Manipulation

// styling elements
// const Title = document.querySelector('#main-heading');
// title.style.color = 'red';
// console.log(title);

// const items = document.querySelectorAll('.list-items');
// for (i = 0; i < items.length; i++) {
//     items[i].style.fontSize = '3rem';
// }

// Creating elements
const ul = document.querySelector('ul');
const li = document.createElement('li');

// Adding elements
ul.append(li)

// Modifying text
li.innerText = 'X-men';

// Modifying attributes & classes
li.setAttribute('id', 'main-heading');
li.removeAttribute('id'); // try removing this line

const mainTitle = document.querySelector('#main-heading');
console.log(mainTitle.getAttribute('id'))

// this adds li to list-items class
li.classList.add('list-items');
console.log(li.classList.contains('list-items'));
// there is also: li.classList.remove('list-items');

// remove elements
li.remove();