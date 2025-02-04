document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const university = document.getElementById('university').value;
    const major = document.getElementById('major').value;
    const year = document.getElementById('year').value;
    const interests = document.getElementById('interests').value;

    // Display a success message
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = `Thank you for registering, ${name}!`;
    
    // Optionally, you can clear the form
    document.getElementById('registrationForm').reset();
});