// function scrapeAmazonData() {
//     var url = document.getElementById("amazon-url").value;
//     var resultDiv = document.getElementById("result");
//     var loader = document.getElementById("loader"); // Loading animation

//     // Show loading animation
//     loader.style.display = "block";

//     // Send AJAX request to scrape data
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4) {
//             // Hide loading animation when request is complete
//             loader.style.display = "none";
//             if (this.status == 200) {
//                 var data = JSON.parse(this.responseText);
//                 if (data.success) {
//                     resultDiv.innerHTML = `
//                         <p><strong>Title:</strong> ${data.title}</p>
//                         <p><strong>Price:</strong> ${data.price}</p>
//                         <p><strong>Discount:</strong> ${data.discount}</p>
//                         <p><strong>MRP:</strong> ${data.mrp}</p>
//                     `;
//                     // Open Flipkart search results in a new tab
//                     window.open(data.flipkart_search_url, "_blank");
//                 } else {
//                     resultDiv.innerHTML = "<p>Failed to retrieve data. Please try again.</p>";
//                 }
//             } else {
//                 resultDiv.innerHTML = "<p>Failed to retrieve data. Please try again.</p>";
//             }
//         }
//     };
//     xhttp.open("GET", "/scrape?url=" + encodeURIComponent(url), true);
//     xhttp.send();
// }



function scrapeAmazonData() {
    var url = document.getElementById("amazon-url").value;
    var resultDiv = document.getElementById("result");
    var loader = document.getElementById("loader"); // Loading animation

    // Show loading animation
    loader.style.display = "block";

    // Send AJAX request to scrape data
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            // Hide loading animation when request is complete
            loader.style.display = "none";
            if (this.status == 200) {
                var data = JSON.parse(this.responseText);
                if (data.success) {
                    resultDiv.innerHTML = `
                        <p><strong>Title:</strong> ${data.title}</p>
                        <p><strong>Price:</strong> ${data.price}</p>
                        <p><strong>Discount:</strong> ${data.discount}</p>
                        <p><strong>MRP:</strong> ${data.mrp}</p>
                        <p><strong>Flipkart Search URL:</strong> <a href="${data.flipkart_search_url}" target="_blank">${data.flipkart_search_url}</a></p>
                    `;
                } else {
                    resultDiv.innerHTML = "<p>Failed to retrieve data. Please try again.</p>";
                }
            } else {
                resultDiv.innerHTML = "<p>Failed to retrieve data. Please try again.</p>";
            }
        }
    };
    xhttp.open("GET", "/scrape?url=" + encodeURIComponent(url), true);
    xhttp.send();
}
