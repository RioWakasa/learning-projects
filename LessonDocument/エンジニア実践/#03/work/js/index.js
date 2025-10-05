function clickHandler(e) {
  const box = document.getElementById("box");
  const p = document.createElement("p");
  p.innerText = "Added by JS";
  box.appendChild(p);
}