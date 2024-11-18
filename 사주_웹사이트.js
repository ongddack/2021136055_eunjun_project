const inputField = document.getElementById("birthdate");

inputField.addEventListener("focus", function () {
  this.placeholder = "";
});

inputField.addEventListener("blur", function () {
  if (this.value === "") {
    this.placeholder = "yyyy / mm / dd";
  }
});
