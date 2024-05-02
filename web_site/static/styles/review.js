$(document).ready(function() {
    var book_id = $("#postform").data("book_id");

    $('#postform').submit(function (event){
        event.preventDefault();
        var review_data = {
        review_text:$("#review_text").val(),
        rating: $("#rating").val()
        };
 
        $.ajax({
            type:"POST",
            url:"/review/" + book_id,
            contentType: "application/json;charset=UTF-8",
            data: JSON.stringify(review_data),
            success: function (response) {
                if (response.success){
                    window.location.href =response.redirect;
                    }
                else {
                    alert("Incorrect");
                    }
            },
            error: function(error) {
                 alert("Error: " + JSON.stringify(error));
            }
        });
    });
    });
