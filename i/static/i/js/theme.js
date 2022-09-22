let themeButton = document.querySelector(".theme-button");
let body = document.querySelector('body');
let a = document.querySelectorAll('a');
let moon = document.querySelector('.moon');
let sun = document.querySelector('.sun');

themeButton.onclick = function() {

    body.classList.toggle('bg-dark');
    body.classList.toggle('text-white');
    
}