document.getElementById('fetchForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const numberId = document.getElementById('numberId').value;
    const resultElement = document.getElementById('result');
    
    try {
        const response = await fetch(`http://localhost:9876/numbers/${numberId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        resultElement.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        resultElement.textContent = `Error: ${error.message}`;
    }
});
