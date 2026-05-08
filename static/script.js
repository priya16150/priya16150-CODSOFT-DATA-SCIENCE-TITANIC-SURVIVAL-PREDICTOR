document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        Pclass: parseInt(document.getElementById('Pclass').value),
        Sex: document.getElementById('Sex').value,
        Age: parseFloat(document.getElementById('Age').value),
        SibSp: parseInt(document.getElementById('SibSp').value),
        Parch: parseInt(document.getElementById('Parch').value),
        Fare: parseFloat(document.getElementById('Fare').value),
        Embarked: document.getElementById('Embarked').value
    };
    
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '🔄 Analyzing passenger data...';
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.prediction === 1) {
            resultDiv.innerHTML = `✅ SURVIVED! (Probability: ${(data.probability * 100).toFixed(1)}%)`;
            resultDiv.className = 'survived';
        } else {
            resultDiv.innerHTML = `❌ DID NOT SURVIVE (Probability: ${(data.probability * 100).toFixed(1)}%)`;
            resultDiv.className = 'died';
        }
    } catch (error) {
        resultDiv.innerHTML = '⚠️ Error making prediction. Please try again.';
        resultDiv.className = '';
    }
});