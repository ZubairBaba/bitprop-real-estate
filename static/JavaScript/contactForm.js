document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('contactForm').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting normally

        // Get form data
        var name = document.getElementById('name').value;
        var contact = document.getElementById('contact').value;
        var email = document.getElementById('email').value;

        // Perform form validation here if needed

        // Send form data to server
        var formData = new FormData();
        formData.append('name', name);
        formData.append('contact', contact);
        formData.append('email', email);

        fetch('/submit_form', {
            method: 'POST',
            body: formData
        })
        .then(function (response) {
            if (response.ok) {
                // Show success message
                document.getElementById('message-container').innerHTML = 'Form submitted successfully!';
                // Clear form fields
                document.getElementById('contactForm').reset();
            } else {
                // Show error message
                document.getElementById('message-container').innerHTML = 'Error submitting form. Please try again later.';
            }
        })
        .catch(function (error) {
            console.error('Error:', error);
            // Show error message
            document.getElementById('message-container').innerHTML = 'Error submitting form. Please try again later.';
        });
    });
});
