document.getElementById("birthdayForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission
    const bornDate = document.getElementById("born_date").value;

    // Cancel any ongoing typing effect before starting a new one
    clearTimeout(window.typeWriterTimeout);

    // Send data to the server
    const response = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `born_date=${encodeURIComponent(bornDate)}`
    });

    const resultText = await response.text();

    // Animate typing effect
    const resultContainer = document.getElementById("result");
    resultContainer.textContent = ""; // Clear previous result

    let i = 0;
    function typeWriter() {
        if (i < resultText.length) {
            resultContainer.textContent += resultText[i];
            i++;
            window.typeWriterTimeout = setTimeout(typeWriter, 50); // Store timeout ID
        }
    }
    typeWriter();
});

// Show footer after 10 seconds
setTimeout(() => {
    const footer = document.getElementById("footer");
    footer.classList.add("visible"); // Adds the visible class to fade in
}, 1000);
