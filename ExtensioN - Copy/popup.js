chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  var currentTab = tabs[0];
  var currentUrl = currentTab.url;

  console.log(currentUrl);

  // Display loading spinner and hide other elements
  document.getElementById('result').innerHTML = '';
  document.getElementById('gen').style.display = 'none';
  document.getElementById('error').style.display = 'none';
  document.getElementById('infoTable').style.display = 'none';
  document.getElementById('spinner').style.display = 'block';

  console.log(currentUrl);
  if (currentUrl.includes("amazon.in")) {
    // Send message to background script to scrape Amazon data
    chrome.runtime.sendMessage({ action: "scrapeAmazonData", url: currentUrl }, function(response) {
      console.log(response);
      if (response.success) {
        // Display scraped data in the popup
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('infoTable').style.display = 'table';
        var title = document.getElementById('title');
        var price = document.getElementById('price');
        var mrp = document.getElementById('mrp');
        var dis = document.getElementById('dis');
        var rate = document.getElementById('rate');
        var fakeUrgency = document.getElementById('fakeUrgency');

        title.innerHTML = response.title;
        price.innerHTML = response.price;
        mrp.innerHTML = response.mrp;
        dis.innerHTML = response.discount;
        rate.innerHTML = response.rate;
        fakeUrgency.innerHTML = response.fakeUrgency;

        // Display warning message if dark pattern detected
        var res = document.getElementById('result');
        res.innerHTML = 'Dark Pattern Detected';
        res.style.color = 'red';
        fakeUrgency.style.backgroundColor = 'red';
      } else {
        // Display error message
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('infoTable').style.display = 'none';
        document.getElementById('error').style.display = 'block';
        document.getElementById('result').innerHTML = "An Error Occured while fetching the data. Please try again.";
      }
    });
  } else {
    // Display message for unsupported sites
    document.getElementById('gen').style.display = 'block';
    document.getElementById('spinner').style.display = 'none';
    document.getElementById('infoTable').style.display = 'none';
    document.getElementById('result').innerHTML = "This extension only works on Amazon.in";
  }
});
