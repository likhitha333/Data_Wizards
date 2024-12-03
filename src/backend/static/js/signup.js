// Select elements
const signupForm = document.getElementById("signupForm");
const errorMessage = document.getElementById("errorMessage");

// Add event listener for form submission
signupForm.addEventListener("submit", function(event) {
    event.preventDefault();

    // Validate form fields
    const firstName = document.getElementById("firstname").value.trim();
    const lastName = document.getElementById("lastname").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    // Basic validation
    if (!firstName || !lastName || !email || !password) {
        showError("All fields are required.");
        return;
    }

    // Validate email format
    if (!validateEmail(email)) {
        showError("Please enter a valid email address.");
        return;
    }

    // Validate password strength
    if (password.length < 6) {
        showError("Password must be at least 6 characters long.");
        return;
    }

    // If validation passes, send data to the backend
    registerUser(firstName, lastName, email, password);
});

// Helper function for email validation
function validateEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

// Function to show error messages
function showError(message) {
    errorMessage.innerText = message;
    errorMessage.style.display = "block";
}

// Function to register user
async function registerUser(firstName, lastName, email, password) {
    try {
        const response = await fetch("http://localhost:5000/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ firstName, lastName, email, password })
        });

        if (response.ok) {
            alert("Registration successful!");
            window.location.href = "login.html"; // Redirect to login page
        } else {
            const data = await response.json();
            showError(data.message || "Failed to register. Please try again.");
        }
    } catch (error) {
        console.error("Error:", error);
        showError("An error occurred. Please try again later.");
    }
}
