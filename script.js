// Date and Time Formats
const formats = [
    { regex: /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/((19|20)\d\d)$/, name: "DD/MM/YYYY" },
    { regex: /^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-((19|20)\d\d)$/, name: "DD-MM-YYYY" },
    { regex: /^((19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/, name: "YYYY-MM-DD" },
    { regex: /^(January|February|March|April|May|June|July|August|September|October|November|December)\s(0[1-9]|[12][0-9]|3[01]),\s((19|20)\d\d)$/, name: "Month DD, YYYY" },
    { regex: /^(0[1-9]|[12][0-9]|3[01])\s(January|February|March|April|May|June|July|August|September|October|November|December)\s((19|20)\d\d)$/, name: "DD Month YYYY" },
    { regex: /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/, name: "HH:MM (24-hour)" },
    { regex: /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$/, name: "HH:MM:SS (24-hour)" },
    { regex: /^(0?[1-9]|1[0-2]):[0-5][0-9]\s(AM|PM)$/, name: "HH:MM AM/PM (12-hour)" },
    { regex: /^(0?[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9]\s(AM|PM)$/, name: "HH:MM:SS AM/PM (12-hour)" },
    { regex: /^((19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$/, name: "YYYY-MM-DD HH:MM:SS (ISO 8601)" },
    { regex: /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/((19|20)\d\d)\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/, name: "DD/MM/YYYY HH:MM" },
    { regex: /^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-((19|20)\d\d)\s(0?[1-9]|1[0-2]):[0-5][0-9]\s(AM|PM)$/, name: "DD-MM-YYYY HH:MM AM/PM" }
];

// Function to validate the input
function validateDateTime(input) {
    const matchingFormats = formats.filter(format => format.regex.test(input));
    return matchingFormats.map(format => format.name);
}

// Detailed Validation
function validateAllFormats(input) {
    return formats.map(format => ({
        name: format.name,
        isValid: format.regex.test(input)
    }));
}

// UI Interaction
document.getElementById("validateButton").addEventListener("click", () => {
    const input = document.getElementById("dateTimeInput").value;
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    if (!input.trim()) {
        resultsDiv.innerHTML = `<div class="alert alert-warning">Please enter a date or time to validate.</div>`;
        return;
    }

    const validFormats = validateDateTime(input);
    const detailedResults = validateAllFormats(input);

    if (validFormats.length > 0) {
        resultsDiv.innerHTML = `
  <div class="alert alert-success">
    The input is valid for the following format(s):
    <ul>
      ${validFormats.map(format => `<li>${format}</li>`).join("")}
    </ul>
  </div>
`;
    } else {
        resultsDiv.innerHTML = `
  <div class="alert alert-danger">
    The input does not match any supported format.
  </div>
`;
    }

    // Show detailed results
    resultsDiv.innerHTML += `
<h5 class="mt-4">Detailed Results:</h5>
<ul>
  ${detailedResults
            .map(
                result =>
                    `<li class="${result.isValid ? "result-valid" : "result-invalid"}">
          ${result.name}: ${result.isValid ? "Valid" : "Invalid"}
        </li>`
            )
            .join("")}
</ul>
`;
});