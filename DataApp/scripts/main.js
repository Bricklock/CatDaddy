

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

document.querySelector("#catIconPicture").onclick = function() {
    alert('Ouch! Stop poking me!');
}

document.addEventListener('DOMContentLoaded', function () {
  var checkbox = document.querySelector('input[type="checkbox"]');
  var page = document.body;
  checkbox.addEventListener('change', function () {
    if (checkbox.checked) {
      page.classList.toggle("light-mode");
      console.log('Light Mode Toggled On');
    } else {
      page.classList.toggle("light-mode");
      console.log('Light Mode Toggled Off');
    }
  });
});
