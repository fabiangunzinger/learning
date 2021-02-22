

svg.selectAll("rect")
    .data(mydata)
    .enter()
    .append("rect")
    .attr("height", h)
    

h = 50;

svg.selectAll("rect")
  .data(data)
  .enter()
  .append("rect")
  .attr("height", "40px")
  .attr("width", function(d) { return d * 50; })
  .attr("y", function(d, i) { return i * 41; })
  .attr("fill", "orange")
  .append("text")
  .attr("color", "black")
  .text(function(d) { d });
