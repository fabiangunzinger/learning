
console.log(data.hexes.UKC12.n);

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
polygons = hexmap
.append("polygon")
  .attr("points", function(hex) { return hex.points; })
  .attr("stroke", "white")
  .attr("stroke-width", "2")
  .attr("fill", "blue");
  
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
