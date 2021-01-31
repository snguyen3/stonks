const ticker = "DogeCoin";
const subreddit = "SatoshiStreetBets";
window.Apex = {
  chart: {
    foreColor: '#ccc',
    toolbar: {
      show: false
    },
  },
  stroke: {
    width: 3
  },
  dataLabels: {
    enabled: false
  },
  tooltip: {
    theme: 'dark'
  },
  grid: {
    borderColor: "#535A6C",
    xaxis: {
      lines: {
        show: true
      }
    }
  }
};

var spark1 = JSON.parse(JSON.stringify(spark_default))
var spark2 = JSON.parse(JSON.stringify(spark_default))
var spark3 = JSON.parse(JSON.stringify(spark_default))
var spark4 = JSON.parse(JSON.stringify(spark_default))

spark1.chart.id = 'spark1';
spark1.series[0].data = [25, 66, 41, 59, 25, 44, 12, 36, 9, 21]
spark1.tooltip.enabled = false;

spark2.chart.id = 'spark2';
spark2.series[0].data = [12, 14, 2, 47, 32, 44, 14, 55, 41, 69]

spark3.chart.id = 'spark3';
spark3.series[0].data = [47, 45, 74, 32, 56, 31, 44, 33, 45, 19]

spark3.chart.id = 'spark4';
spark3.series[0].data = [15, 75, 47, 65, 14, 32, 19, 54, 44, 61]


new ApexCharts(document.querySelector("#spark1"), spark1).render();
new ApexCharts(document.querySelector("#spark2"), spark2).render();
new ApexCharts(document.querySelector("#spark3"), spark3).render();
new ApexCharts(document.querySelector("#spark4"), spark4).render();


var stonkOptions = JSON.parse(JSON.stringify(defaultLineOptions));
seriesData = generateTimeSeriesData(38.2, 45.0, new Date(2019, 1, 1, 0, 0, 0), new Date(), 24 * 14)
stonkOptions.id = "Stonk Chart"
stonkOptions.series[0] = {
  'data': seriesData.map(function (pair) { return [pair[0], seriesData[0][1] * 2 - pair[1] * 0.5] }),
  'name': "DogeCoin"
};
stonkOptions.series.push({
  'data': seriesData,
  'name': "GME"
});
stonkOptions.title = {
  text: `${ticker}`,
  align: 'left',
}
stonkOptions.subtitle = {
  
  text: 'Stonk Price',
}
stonkOptions.legend = {
  position: 'top',
  horizontalAlign: 'right',
}


var sentimentOptions = JSON.parse(JSON.stringify(defaultLineOptions));
sentimentOptions.id = "Sentiment Chart"
sentimentOptions.title = {
  text: `${ticker}`,
  align: 'left',
}
sentimentOptions.subtitle = {
  text: `Sentiment on reddit.com/r/${subreddit}`,
}
sentimentOptions.legend = {
  position: 'top',
  horizontalAlign: 'right',
}
sentimentOptions.series[0] = {
  'data': seriesData.map(function (pair) { return [pair[0], pair[1] * 2] }),
  'name': "DogeCoin"
};
sentimentOptions.series.push({
  'data': seriesData,
  'name': "GME"
});


var sentimentChart = new ApexCharts(
  document.querySelector("#sentiment-chart"),
  sentimentOptions
);
var stonkChart = new ApexCharts(
  document.querySelector('#stonk-chart'),
  stonkOptions);

sentimentChart.render();
stonkChart.render();



var resetCssClasses = function (activeEl) {
  var els = document.querySelectorAll("button");
  Array.prototype.forEach.call(els, function (el) {
    el.classList.remove('active');
  });

  activeEl.target.classList.add('active')
};




// Button Event Handlers
chartsToUpdate = [sentimentChart, stonkChart];
document.querySelector("#one_month").addEventListener('click', function (e) {
  resetCssClasses(e);
  for (chart of chartsToUpdate) {
    chart.updateOptions({
      xaxis: {
        min: new Date(
          new Date().getFullYear(),
          new Date().getMonth() - 1,
          new Date().getDate()).getTime(),
        max: new Date().getTime()
      }
    })
  }
});

document.querySelector("#six_months").addEventListener('click', function (e) {
  resetCssClasses(e);
  for (chart of chartsToUpdate) {

    chart.updateOptions({
      xaxis: {
        min: new Date(
          new Date().getFullYear(),
          new Date().getMonth() - 6,
          new Date().getDate()).getTime(),
        max: new Date().getTime()
      }
    })
  }
});

document.querySelector("#one_year").addEventListener('click', function (e) {
  resetCssClasses(e);
  for (chart of chartsToUpdate) {

    chart.updateOptions({
      xaxis: {
        min: new Date(
          new Date().getFullYear() - 1,
          new Date().getMonth(),
          new Date().getDate()).getTime(),
        max: new Date().getTime()
      }
    })
  }
});

document.querySelector("#ytd").addEventListener('click', function (e) {
  resetCssClasses(e);
  for (chart of chartsToUpdate) {

    chart.updateOptions({
      xaxis: {
        min: new Date(
          new Date().getFullYear(),
          0,
          1).getTime(),
        max: new Date().getTime()
      }
    })
  }
});

document.querySelector("#all").addEventListener('click', function (e) {
  resetCssClasses(e);
  for (chart of chartsToUpdate) {
    chart.updateOptions({
      xaxis: {
        min: undefined,
        max: undefined
      }
    })
  }
});

document.querySelector("#ytd").addEventListener('click', function () {

});


