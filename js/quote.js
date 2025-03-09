function fetchQuote() {
    fetch("http://127.0.0.1:5000/quote")
    .then(response => response.json())
    .then(data => {
        document.getElementById("quote-text").innerText = data.quote;
    })
    .catch(error => console.error("Error fetching quote:", error));
}
