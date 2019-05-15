function _profile() {
  document.getElementById("_profile").style.display = "block";
  document.getElementById("_password").style.display = "none";
  document.getElementById("_email").style.display = "none";
  document.getElementById("_friends").style.display = "none";
  document.getElementById("_privacy").style.display = "none";
}

function _password() {
  document.getElementById("_profile").style.display = "none";
  document.getElementById("_password").style.display = "block";
  document.getElementById("_email").style.display = "none";
  document.getElementById("_friends").style.display = "none";
  document.getElementById("_privacy").style.display = "none";
}

function _email() {
  document.getElementById("_profile").style.display = "none";
  document.getElementById("_password").style.display = "none";
  document.getElementById("_email").style.display = "block";
  document.getElementById("_friends").style.display = "none";
  document.getElementById("_privacy").style.display = "none";
}

function _friends() {
  document.getElementById("_profile").style.display = "none";
  document.getElementById("_password").style.display = "none";
  document.getElementById("_email").style.display = "none";
  document.getElementById("_friends").style.display = "block";
  document.getElementById("_privacy").style.display = "none";
}

function _privacy() {
  document.getElementById("_profile").style.display = "none";
  document.getElementById("_password").style.display = "none";
  document.getElementById("_email").style.display = "none";
  document.getElementById("_friends").style.display = "none";
  document.getElementById("_privacy").style.display = "block";
}
