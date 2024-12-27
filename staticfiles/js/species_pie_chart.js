
const canvas = document.getElementById('speciesPieChart');
const labels = JSON.parse(canvas.getAttribute('data-labels'));
const data = JSON.parse(canvas.getAttribute('data-data'));
new Chart(ctx, {
    type: 'pie',
    data: {
        labels: labels,
        datasets: [{
            label: 'Sample Count',
            data: data,
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true, 
        plugins: {
            legend: {
                position: 'top',
            }
        }
    }
});
