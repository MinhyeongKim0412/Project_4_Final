function showResults(tab) {
    const results = document.querySelectorAll('.results');
    const tabs = document.querySelectorAll('.tab');
    results.forEach(result => {
        result.classList.remove('active-results');
    });
    tabs.forEach(t => {
        t.classList.remove('active');
    });

    document.getElementById(tab).classList.add('active-results');
    const activeTab = Array.from(tabs).find(t => t.innerText === tab.charAt(0).toUpperCase() + tab.slice(1));
    if (activeTab) {
        activeTab.classList.add('active');
    }
}