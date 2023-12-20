

$(document).ready(function() {
    // form submission logic
    $("#form_data").submit(function(e) {
        e.preventDefault();
        
        // show loading modal on success
        $('#loadingModal').show();

        $.ajax({
            url: '{% url "home" %}',
            type: 'POST',
            data: new FormData(this),
            headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},
            processData: false,
            contentType: false,
            dataType: 'json',
            success: function(response) {

                // Hide loading modal on success
                $('#loadingModal').hide();

                if (response.status === "success") {
                // Handle success (maybe redirect or display a success message)
                // console.log(response);
                    alert("Success: " + response.message);
                    $("#form_data")[0].reset();
                } 
                else if(response.status === "error"){
                    // Display error message to the user
                    // console.log(response);
                    alert("Error: " + response.message);
                }
            },

            error: function(response) {

                // Hide loading modal on success
                $('#loadingModal').hide();

                // Handle other errors (e.g., server error)
                alert('An error occurred while processing your request. Please try again later.');
            }



        });
    });
});