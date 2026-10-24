
// ====================================
// Smart Agriculture Recommendation System
// ====================================

// Render prediction text as DOM content so model output is never treated as HTML.
function showResult(elementId, message, isError = false) {
    const resultBox = document.getElementById(elementId);
    const symbol = document.createElement("span");
    const copy = document.createElement("span");
    const label = document.createElement("span");
    const value = document.createElement("strong");

    symbol.className = "result-symbol";
    symbol.setAttribute("aria-hidden", "true");
    symbol.textContent = isError ? "!" : "🌱";
    copy.className = "result-copy";
    label.className = "result-label";
    label.textContent = isError ? "Something needs your attention" : "Recommendation ready";
    value.className = "result-value";
    value.textContent = message;
    copy.append(label, value);
    resultBox.replaceChildren(symbol, copy);
    resultBox.classList.add("show");
    resultBox.classList.toggle("error", isError);
}

// Reflect only values entered by the user; this panel is not a live weather feed.
function updateWeatherValue(input) {
    const outputId = input.name === "temperature"
        ? "weatherTemperature"
        : "weatherHumidity";
    const output = document.getElementById(outputId);
    const value = document.createTextNode(input.value.trim() || "—");
    const unit = document.createElement("small");

    unit.textContent = input.name === "temperature" ? "°C" : "%";
    output.replaceChildren(value, unit);
}

document.querySelectorAll(
    '#cropForm [name="temperature"], #cropForm [name="humidity"], ' +
    '#fertilizerForm [name="temperature"], #fertilizerForm [name="humidity"]'
).forEach(function (input) {
    input.addEventListener("input", function () {
        updateWeatherValue(input);
    });
});


// Send form data to the Flask backend
async function getRecommendation(form, endpoint, resultId, buttonText) {
    const submitButton = form.querySelector('button[type="submit"]');

    // Convert form fields into a JavaScript object
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Convert numeric form values into numbers
    for (const key in data) {
        if (data[key].trim() !== "" && !isNaN(data[key])) {
            data[key] = Number(data[key]);
        }
    }

    submitButton.disabled = true;
    submitButton.textContent = "Processing...";

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error(
                result.message || "Unable to generate a recommendation."
            );
        }

        showResult(
            resultId,
            "🌱 Recommended result: " + result.recommendation
        );

    } catch (error) {
        console.error("Recommendation error:", error);

        showResult(
            resultId,
            error.message || "Something went wrong. Please try again.",
            true
        );

    } finally {
        submitButton.disabled = false;
        submitButton.textContent = buttonText;
    }
}


// ====================================
// Crop Recommendation Form
// ====================================

const cropForm = document.getElementById("cropForm");

cropForm.addEventListener("submit", function (event) {
    event.preventDefault();

    getRecommendation(
        cropForm,
        "/recommend_crop",
        "cropResult",
        "Recommend Crop"
    );
});


// ====================================
// Fertilizer Recommendation Form
// ====================================

const fertilizerForm = document.getElementById("fertilizerForm");

fertilizerForm.addEventListener("submit", function (event) {
    event.preventDefault();

    getRecommendation(
        fertilizerForm,
        "/recommend_fertilizer",
        "fertilizerResult",
        "Recommend Fertilizer"
    );
});
