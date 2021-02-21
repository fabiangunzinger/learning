var barHeight = Math.floor(height / data.length);

var bars = r2d3.svg.selectAll('rect')
.data(r2d3.data);

bars.enter()
.append('rect')
.attr('width', function(d) { return d * width; })
.attr('height', barHeight)
.attr('y', function(d, i) { return i * barHeight; })
.attr('fill', 'steelblue');

bars.exit().remove();

bars.transition()
.duration(100)
.attr("width", function(d) { return d * width; });


// my example code

var bars = r2d3.svg;

bars.selectAll('circle')
.data(r2d3.data)
.enter()
.append('circle')
.attr("fill", "grey")
.attr("cx", function(d, i) {return (i * 50) + 20})
.attr("cy", function(d, i) {return (i * 50) + 20})
.attr("r", function(d) {return d * 100; });

bars.transition()
.duration(100)
.attr("r", function(d) {return d * 100; });
