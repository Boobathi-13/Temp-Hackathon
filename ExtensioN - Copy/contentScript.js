// contentScript.js
const currentUrl = window.location.href;
chrome.runtime.sendMessage({ action: "getTabUrl" }, function(response) {
    const tabUrl = response.url;
});
