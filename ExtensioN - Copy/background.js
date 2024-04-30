chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "scrapeAmazonData") {
    fetch('http://localhost:5000/scrape', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: request.url }),
    })
    .then(response => response.json())
    .then(data => sendResponse(data))
    .catch(error => sendResponse({ success: false }));
    return true; // Indicates that sendResponse will be called asynchronously
  }
});
