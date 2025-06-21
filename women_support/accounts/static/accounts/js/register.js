function togglePassword(id) {
  const field = document.getElementById(id);
  if (field.type === "password") {
    field.type = "text";
  } else {
    field.type = "password";
  }
}
