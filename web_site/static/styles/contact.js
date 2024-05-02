//
$(document).ready(function () {
     $("#contact_form").submit(function (event) {
        event.preventDefault();
        
        var formData = {
            name: $("#name").val(),
            email: $("#email").val(),
            phone_number: $("#phone_number").val(),
            message_box: $("#message_box").val()
        };
        $.ajax({
            type: "POST",
            url: "/contact-us",
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
