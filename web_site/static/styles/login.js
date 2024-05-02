//
$(document).ready(function() {
    $("#loginform").submit(function (event){
        event.preventDefault();
        var data = {
        email:$("#email").val(),
        password: $("#password").val()
        };
        
        $.ajax({
            type:"POST",
            url: "/login",
            contentType: "application/json;charset=UTF-8",
            data: JSON.stringify(data),
            success: function (response) {
                if (response.success){
                    window.location.href = response.redirect;
                    }
                else {
                    document.getElementById("incorrect").innerHTML = "Incorrect credentials ";
                    }
            },
            error: function (error) {
                alert("Error: " + JSON.stringify(error));
                }
        });
    });
});
