// Define SVG area dimensions
var svgWidth = 960;
// Load data from csv
d3.json("/chartstay").then(function(chartData) {

  console.log(chartData)

  //   weekPos = [1, 4, 7, 9]
  //   peakPos = [2, 5, 8, 2]
    
  //   var trace1 = {
  //     type: "scatter",
  //     mode: "lines",
  //     name: "my plot",
  //     x: weekPos,
  //     y: peakPos,
  //     line: {
  //       color: "#17BECF"
  //     }
  //   };

  //   var data = [trace1];

  //   Plotly.newPlot("plot", data)
  // 
})