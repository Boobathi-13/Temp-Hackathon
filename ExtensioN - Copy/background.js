chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "scrapeAmazonData") {
      fetch('http://localhost:5000/scrape?url=' + encodeURIComponent(request.url))
        .then(response => response.json())
        .then(data => sendResponse(data))
        .catch(error => console.error('Error:', error))
      return true; // Indicates that sendResponse will be called asynchronously
    }
  });
