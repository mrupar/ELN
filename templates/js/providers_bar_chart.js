document.addEventListener("DOMContentLoaded", function () {
    const labels = JSON.parse(document.getElementById("providersBarChart").dataset.labels);
    const data = JSON.parse(document.getElementById("providersBarChart").dataset.data);

    const ctx = document.getElementById('providersBarChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Number of Provided Samples',
                data: data,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Sample Providers and their Provided Samples'
                }
            }
        }
    });
});

