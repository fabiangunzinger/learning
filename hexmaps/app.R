library(shiny)
library(r2d3)

ui <- fluidPage(
  inputPanel(
    sliderInput("bar_max", label = "Max:",
                min = 0, max = 1, value = 1, step = 0.05)
  ),
  textOutput("d3")
)

server <- function(input, output) {
  output$d3 <- renderD3({
    r2d3(
      "/Users/fgu/dev/projects/learning/hexmaps/nuts3.hexjson",
      script = file.path("/Users/fgu/dev/projects/learning/hexmaps/map.js")
    )
  })
}

shinyApp(ui = ui, server = server)