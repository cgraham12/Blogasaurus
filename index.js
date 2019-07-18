console.log("I'm working!")

const title = document.querySelector('#Title');
title.addEventListener('click', (e) => {
  document.querySelector("#title").style.backgroundColor = "Red";
  document.querySelector("#title").innerHTML = "Red"
});
