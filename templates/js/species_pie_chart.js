document.addEventListener("DOMContentLoaded", function () {
    const labels = JSON.parse(document.getElementById("speciesPieChart").dataset.labels);
    const data = JSON.parse(document.getElementById("speciesPieChart").dataset.data);

    const ctx = document.getElementById('speciesPieChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Sample Count',
                data: data,
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                },
                title: {
                    display: true,
                    text: 'Samples by Species',
                },
            }
        }
    });
});
