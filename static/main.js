let map;

function startTracking() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition((position) => {
      const { latitude, longitude } = position.coords;
      console.log("Tracking:", latitude, longitude);

      if (!map) {
        map = L.map('map').setView([latitude, longitude], 16);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
      }

      L.marker([latitude, longitude]).addTo(map);

      fetch('/check_risk', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ latitude, longitude })
      })
      .then(res => res.json())
      .then(data => {
        const riskBox = document.getElementById('risk-alert');
        if (data.risk) {
          riskBox.textContent = "⚠️ " + data.risk;
          riskBox.style.display = 'block';
        } else {
          riskBox.style.display = 'none';
        }
      });
    });
  } else {
    alert("Geolocation not supported on this device.");
  }
}

function sendSOS() {
  fetch('/sos', { method: 'POST' })
    .then(() => {
      alert("🚨 SOS sent to your contacts!");
    })
    .catch(() => {
      alert("❌ SOS failed. Try again.");
    });
}
