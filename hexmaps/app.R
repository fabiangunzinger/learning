library(jsonlite)
library(shiny)
library(r2d3)
library(htmltools)


hexjson <- "/Users/fgu/dev/projects/learning/hexmaps/nuts3.hexjson"
script <- file.path("/Users/fgu/dev/projects/learning/hexmaps/map.js")


library(shiny)
library(r2d3)

ui <- fluidPage(
  inputPanel(
    sliderInput("bar_max", label = "Max:",
                min = 0.1, max = 1.0, value = 0.2, step = 0.1)
  ),
  d3Output("d3")
)

server <- function(input, output) {
  output$d3 <- renderD3({
    r2d3(
      data = jsonlite::read_json(hexjson),
      script = "./js/map.js",
      dependencies = "d3-hexjson-1.1.0/build/d3-hexjson.min.js"
    )
  })
}

shinyApp(ui = ui, server = server)

