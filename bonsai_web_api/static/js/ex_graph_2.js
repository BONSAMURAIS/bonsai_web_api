function graph_2(){

    var chart = nv.models.multiBarChart();
    chart.margin({top: 30, right: 60, bottom: 40, left: 80});
     chart.yAxis
                .axisLabel("kg CO2-eq.")
                .tickFormat(d3.format(',.02f'))
                .axisLabelDistance(10);
d3.select('#chart_2').datum([
  {
    key: "Aluminium production",
    color: "#1f77b4",
    values:
    [      
      { x : "Raw materials extraction", y : 40 },
      { x : "Supply", y : 30 },
      { x : "Manufacture",   y : 20 }  
    ]
  },
  {
    key: "Re-processing of secondary aluminium",
    color: "#bd362f",
    values:
    [      
      { x : "Raw materials extraction", y : 60 },
      { x : "Supply", y : 50 },
      { x : "Manufacture",   y : 70 } 
    ]
  }
,
  {
    key: "Minim of aluminium ores",
    color: "#ff7f0e",
    values:
    [      
      { x : "Raw materials extraction", y : 15 },
      { x : "Supply", y : 90 },
      { x : "Manufacture",   y : 10 } 
    ]
  }
]).transition().duration(500).call(chart);
};