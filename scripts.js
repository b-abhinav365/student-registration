document.getElementById("regForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var course = document.getElementById("course").value;
    var msg = document.getElementById("message");
  
    if (name == "" || email == "" || phone == "" || course == "") {
      msg.innerHTML = "Please fill all fields";
    } else if (!email.includes("@")) {
      msg.innerHTML = "Invalid email";
    } else if (phone.length != 10 || isNaN(phone)) {
      msg.innerHTML = "Phone must be 10 digits";
    } else {
      msg.innerHTML = "Registration successful";
    }
  });