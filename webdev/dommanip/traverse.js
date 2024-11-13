// DOM traverse
let ul = document.querySelector('ul');
console.log(ul.parentNode);
console.log(ul.childNodes); // indent in html is counted as text node
console.log(ul.firstChild);
console.log(ul.lastChild);
console.log(ul.previousElementSibling);
console.log(ul.nextElementSibling);
ul.childNodes[1].style.backgroundColor = "red";

// you can also use these
// console.log(ul.children)
// console.log(ul.firstElementChild) // element is tag
// console.log(ul.lastElementChild) // node is node in DOM


const html = document.documentElement;
console.log(html.parentNode); // parent node is parent node (docuement included)
console.log(html.parentElement); // parent element is parent tag

