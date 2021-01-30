var spark_default = {
    chart: {
        id: 'NEEDS TO BE SET', // MUST SET ID!!
        group: 'sparks',
        type: 'line',
        height: 80,
        sparkline: {
            enabled: true
        },
        dropShadow: {
            enabled: true,
            top: 1,
            left: 1,
            blur: 2,
            opacity: 0.2,
        }
    },
    series: [{
        data: []
    }],
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 0
    },
    grid: {
        padding: {
            top: 20,
            bottom: 10,
            left: 110
        }
    },
    colors: ['#fff'],
    tooltip: {
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function formatter(val) {
                    return '';
                }
            }
        }
    }
}

var defaultLineOptions = {
    annotations: {
        yaxis: [{
            y: 30,
            borderColor: '#999',
            label: {
                show: true,
                text: 'Support',
                style: {
                    color: "#fff",
                    background: '#00E396'
                }
            }
        }],
        legend: {
            position: 'top',
            horizontalAlign: 'right',
            offsetY: -20
        },
        xaxis: [{
            x: new Date('16 Jan 2021').getTime(),
            borderColor: '#999',
            yAxisIndex: 0,
            label: {
                show: true,
                text: 'Biden Elected',
                style: {
                    color: "#fff",
                    background: '#775DD0'
                }
            }
        }]
    },
    chart: {
        height: 328,
        type: 'line',
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: true,
            top: 3,
            left: 2,
            blur: 4,
            opacity: 1,
        }
    },
    stroke: {
        curve: 'smooth',
        width: 2
    },
    dataLabels: {
        enabled: false
    },
    series: [{
        data: []
    }],
    markers: {
        size: 2,
        strokeWidth: 0,
        hover: {
            size: 9
        }
    },
    xaxis: {
        type: 'datetime',
        min: new Date('01 Jan 2019').getTime(),
        tickAmount: 6
    },
    tooltip: {
        x: {
            format: 'dd MMM yyyy'
        }
    },
    yaxis: {
        decimalsInFloat: 2
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            opacityTo: 0.9,
            stops: [0, 100]
        }
    }
};