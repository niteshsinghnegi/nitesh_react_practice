\<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real-Time Bus Tracking</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        #map { height: 100vh; width: 100%; }
        body { margin: 0; padding: 0; }
    </style>
</head>
<body>
    <div id="map"></div>

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        // Initialize map centered at India
        var map = L.map('map').setView([26.8467, 80.9462], 6);

        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data © OpenStreetMap contributors'
        }).addTo(map);

        // Object to store bus markers
        var busMarkers = {};

        // Fetch buses from backend every 5 seconds
        async function fetchBuses() {
            try {
                const response = await fetch('http://127.0.0.1:8000/buses/');
                const buses = await response.json();

                buses.forEach(bus => {
                    if (busMarkers[bus.id]) {
                        // Update existing marker
                        busMarkers[bus.id].setLatLng([bus.latitude, bus.longitude]);
                    } else {
                        // Add new marker
                        const marker = L.marker([bus.latitude, bus.longitude])
                            .addTo(map)
                            .bindPopup(`<b>${bus.bus_number}</b><br>Lat: ${bus.latitude.toFixed(5)}<br>Lng: ${bus.longitude.toFixed(5)}`);
                        busMarkers[bus.id] = marker;
                    }
                });
            } catch (err) {
                console.error('Error fetching buses:', err);
            }
        }

        // Initial fetch
        fetchBuses();
        // Update every 5 seconds
        setInterval(fetchBuses, 5000);
    </script>
</body>
</html>
