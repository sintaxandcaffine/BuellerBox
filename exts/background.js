// background.js
chrome.runtime.onInstalled.addListener(() => {
  console.log("✅ Bueller Tab Bridge installed.");
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getTabs") {
    chrome.tabs.query({}, (tabs) => {
      const tabData = tabs.map(t => ({ title: t.title, url: t.url }));
      fetch("http://localhost:5000/tabs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tabs: tabData })
      }).then(() => {
        console.log("✅ Tabs sent to Bueller Box.");
      }).catch(err => {
        console.error("❌ Failed to send tabs:", err);
      });
      sendResponse({ status: "sent", count: tabData.length });
    });
    return true; // keep message channel alive for async response
  }
});
