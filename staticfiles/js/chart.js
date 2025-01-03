document.addEventListener("DOMContentLoaded", function () {
    // Reusable function to create charts
    function createChart(chartId, chartType, chartLabels, chartData, chartTitle, chartLegend='') {
        const ctx = document.getElementById(chartId).getContext('2d');
        new Chart(ctx, {
            type: chartType,
            data: {
                labels: chartLabels,
                datasets: [{
                    data: chartData,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: chartLegend,
                    },
                    title: {
                        display: true,
                        text: chartTitle,
                    }
                },
                scales: chartType === 'bar' ? {
                    y: {
                        beginAtZero: true
                    }
                } : undefined
            }
        });
    }

    // Ensure each canvas has its unique ID
    createChart(
        "speciesPieChart", // ID
        "pie", // Type
        JSON.parse(document.getElementById("speciesPieChart").dataset.labels), // Labels
        JSON.parse(document.getElementById("speciesPieChart").dataset.data), // Data
        document.getElementById("speciesPieChart").dataset.title, // Title
        'bottom', // Legend position
    );

    createChart(
        "projectsPieChart", // ID
        "pie", // Type
        JSON.parse(document.getElementById("projectsPieChart").dataset.labels), // Labels
        JSON.parse(document.getElementById("projectsPieChart").dataset.data), // Data
        document.getElementById("projectsPieChart").dataset.title, // Title
        'bottom', // Legend position
    );

    createChart(
        "providersBarChart", // ID
        "bar", // Type
        JSON.parse(document.getElementById("providersBarChart").dataset.labels), // Labels
        JSON.parse(document.getElementById("providersBarChart").dataset.data), // Data
        document.getElementById("providersBarChart").dataset.title // Title
    );
});
