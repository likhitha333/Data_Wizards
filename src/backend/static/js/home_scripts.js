// Select elements
const goalForm = document.getElementById("goalForm");
const waterForm = document.getElementById("waterForm");
const notificationArea = document.getElementById("notificationArea");

// Initialize variables
let dailyGoal = parseInt(localStorage.getItem("dailyGoal")) || 0;
let currentIntake = parseInt(localStorage.getItem("currentIntake")) || 0;

// Check for date change
const today = new Date().toLocaleDateString();
const storedDate = localStorage.getItem("date");

if (storedDate !== today) {
    // If the date has changed, reset currentIntake
    currentIntake = 0;
    localStorage.setItem("currentIntake", currentIntake);
    localStorage.setItem("date", today); // Update the stored date
}

// Display initial goal and intake
document.getElementById("dailyGoal").value = dailyGoal || '';
updateIntakeDisplay();

// Set Daily Goal
goalForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const goalInput = document.getElementById("dailyGoal").value;

    if (!isValidNumber(goalInput)) {
        showNotification("Please enter a valid daily goal!");
        return;
    }

    dailyGoal = parseInt(goalInput);
    localStorage.setItem("dailyGoal", dailyGoal);
    currentIntake = 0; // Reset intake when a new goal is set
    localStorage.setItem("currentIntake", currentIntake);
    updateIntakeDisplay();
    showNotification(`Daily goal set to ${dailyGoal} ml. Start logging your water intake!`);
});

// Log Water Intake
waterForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const waterInput = document.getElementById("waterAmount").value;

    if (!isValidNumber(waterInput)) {
        showNotification("Please enter a valid water amount!");
        return;
    }

    const waterAmount = parseInt(waterInput);
    currentIntake += waterAmount;
    localStorage.setItem("currentIntake", currentIntake);
    updateIntakeDisplay();
    checkGoalStatus();
    document.getElementById("waterAmount").value = ""; // Clear input
});

// Update Intake Display
function updateIntakeDisplay() {
    document.getElementById("goalSection").querySelector("h2").innerText = `Today's Goal: ${currentIntake}/${dailyGoal} ml`;
}

// Check if Goal is Met
function checkGoalStatus() {
    if (currentIntake >= dailyGoal) {
        let message = `🎉 Congratulations! You've reached your daily goal of ${dailyGoal} ml!`;
        if (currentIntake > dailyGoal) {
            message += ` You've even exceeded it with a total of ${currentIntake} ml! 🏆 Keep it up!`;
        }
        showNotification(message);
    } else if (currentIntake >= dailyGoal * 0.8) {
        showNotification("You're close to reaching your daily goal. Keep going!");
    } else {
        const remaining = dailyGoal - currentIntake;
        showNotification(`Great job! You've logged ${currentIntake} ml. Only ${remaining} ml to go!`);
    }
}

// Show Notification
function showNotification(message) {
    notificationArea.innerText = message;
    notificationArea.classList.add("show");
    setTimeout(() => {
        notificationArea.classList.remove("show");
    }, 5000); // Hide after 5 seconds
}

// Utility function to check if a number is valid
function isValidNumber(value) {
    return !isNaN(value) && value > 0;
}
