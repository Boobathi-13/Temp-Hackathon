chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  var currentTab = tabs[0];
  var currentUrl = currentTab.url;

  console.log(currentUrl);

  document.getElementById('result').innerHTML = '';
  document.getElementById('gen').style.display = 'none';
  document.getElementById('error').style.display = 'none';
  document.getElementById('infoTable').style.display = 'none';
  document.getElementById('spinner').style.display = 'block';

  console.log(currentUrl);
  if(currentUrl.includes("amazon.in")){
    chrome.runtime.sendMessage({ action: "scrapeAmazonData", url: currentUrl }, function(response) {
      console.log(response);
      if (response.success) {
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('infoTable').style.display = 'table';
        var title = document.getElementById('title');
        var price = document.getElementById('price');
        var mrp = document.getElementById('mrp');
        var lp = document.getElementById('lp');
        var dis = document.getElementById('dis');
        var adisc = document.getElementById('adisc');
        var rate = document.getElementById('rate');
        var res = document.getElementById('result');
        var fakeUrgency = document.getElementById('fakeUrgency');

        title.innerHTML = response.title;
        price.innerHTML = response.price;
        mrp.innerHTML = response.mrp;
        // lp.innerHTML = null; // Assuming launch price is not provided
        dis.innerHTML = response.discount;
        // adisc.innerHTML = null; // Assuming you don't need actual discount in this case
        rate.innerHTML = response.rate;
        fakeUrgency.innerHTML = response.fakeUrgency;

        res.innerHTML = 'Dark Pattern Detected'; // Assuming there's no dark pattern
        // adisc.style.backgroundColor = 'green';
        fakeUrgency.style.backgroundColor = 'red';
        // res.style.color = 'green';
        res.style.color = 'red';
      } else {
        document.getElementById('spinner').style.display = 'none';
        document.getElementById('infoTable').style.display = 'none';
        document.getElementById('error').style.display = 'block';
        document.getElementById('result').innerHTML = "An Error Occured while fetching the data. Please try again.";
      }
    });
  }
  else{
    document.getElementById('gen').style.display = 'block';
    document.getElementById('spinner').style.display = 'none';
    document.getElementById('infoTable').style.display = 'none';
    document.getElementById('result').innerHTML = "This extension only works on Amazon.in";
  }
});
