// Define SVG area dimensions
// Load data from csv

// function that plots bar charts
function plotBarChart(data, chart_div){
let trace1 = {
  type: "bar",
  name: "my plot",
  x: [],
  y: [],
};
data.forEach(function (val) {
  trace1.x.push(val["x_vals"]);
  trace1.y.push(val["y_vals"])
})

let layout = {
  title: "plot",
  yaxis: { title: "x axis" },
  xaxis: { title: "y axis",
            tickangle: 90
}
}
var data = [trace1];

Plotly.newPlot(chart_div, data, layout)
}

// function that plots pie charts
// not in use right now. 
// But you can always call it when you have data
function plotPieChart(data, chart_div){
  let trace1 = {
    type: "pie",
    name: "my plot",
    values: [],
    labels: [],
  };
  data.forEach(function (val) {
    trace1.values.push(val["x_vals"]);
    trace1.labels.push(val["y_vals"])
  })
  
  let layout = {
    height: 500,
    width: 570
  }
  var data = [trace1];
  
  Plotly.newPlot(chart_div, data, layout)
  }



function plotcharts(){
// this is related to the rout and calls the bar chart function
d3.json("/charttopstay").then(function (chartData) {
  plotBarChart(chartData, "plot")
  
})


d3.json("/chartstay").then(function (chartData) {
  plotBarChart(chartData, "plot2")
})

}