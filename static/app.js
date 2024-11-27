const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
var checker = document.getElementById('cb1');
var sendbtn = document.getElementById('btnlogin');

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
checker.onchange = function () {
  console.log("hello");
  sendbtn.disabled = !this.checked;
};
