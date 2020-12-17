// Define SVG area dimensions
var svgWidth = 960;
// Load data from csv
d3.json("/chartstay").then(function (chartData) {

  console.log(chartData)



  let trace1 = {
    type: "scatter",
    mode: "lines",
    name: "my plot",
    x: [],
    y: [],
    line: {
      color: "#17BECF"
    }
  };
  chartData.foreach(function (val) {
    trace1.x.push(val["x_vals"]);
    trace1.x.push(val["y_vals"])
  })

  let layout = {
    title: "plot",
    yaxis: { title: "y axis" },
    xaxis: { title: "y axis" }
  }
  var data = [trace1];

  Plotly.newPlot("plot", data, layout)
  // 

})
