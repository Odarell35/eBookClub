//
$(document).ready(function () {
     $("#signupForm").submit(function (event) {
        event.preventDefault();
        
        var formData = {
            name: $("#name").val(),
            surname: $("#surname").val(),
            email: $("#email").val(),
            password: $("#password").val()
        };
        $.ajax({
            type: "POST",
            url: "/sign-up",
            contentType: "application/json;charset=UTF-8",
            data: JSON.stringify(formData),
            success: function (response) {
                if (response.success){
                    window.location.href = response.redirect;
                }
                else {
                    alert("Incorrect credentials");
                    }
             },
            error: function (error) {
            alert("Error: " + JSON.stringify(error));
            }
        });
    });
 });
