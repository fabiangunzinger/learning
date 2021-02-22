var hexes = d3.renderHexJSON(data, width, height);

// bind hexes to g elements and position them
var hexmap = svg.selectAll("g")
.data(hexes)
.enter()
.append("g")
.attr("transform", function(hex) {
  return "translate(" + hex.x + ", " + hex.y + ")";
});

// draw the polygons around each hex's centre
var polygons = hexmap
.append("polygon")
  .attr("points", function(hex) { return hex.points; })
  .attr("stroke", "white")
  .attr("stroke-width", "2")
  .attr("fill", "blue");

polygons
  .on("click", function(d) {
    var xpos = parseFloat(d3.select(this).attr(x));
    var ypos = parseFloat(d3.select(this).attr(y));
    svg.append("text")
      .attr("id", "tooltip")
      .attr("x", xpos)
      .attr("y", ypos)
      .attr("fill", "orange")
      .text(d);
  })

polygons
  .on("mouseover", function() {
    d3.select(this)
      .attr("stroke-width", "4")
      .attr("fill", "orange");
  })
  .on("mouseout", function() {
    d3.select(this)
      .attr("stroke-width", "2")
      .attr("fill", "blue");
  });