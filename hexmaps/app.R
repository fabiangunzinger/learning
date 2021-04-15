library(jsonlite)
library(shiny)
library(r2d3)
library(htmltools)

ui <- fluidPage(
  selectInput(
    inputId = "geonm",
    label = "Geography",
    choices = c("nuts3", "lad", "constituencies"),
    selected = "lad"
  ),
  d3Output("d3"),
  textOutput("msg"),
  tableOutput("tab")
)

server <- function(input, output) {
  
  data <- reactive({ 
    path = "/Users/fgu/dev/projects/learning/hexmaps/data"
    fn = paste0(input$geonm, '.hexjson')
    fp = file.path(path, fn)
    return(jsonlite::read_json(fp))
  })
  
  output$d3 <- renderD3({
    r2d3(
      data = data(),
      script = "./js/map.js",
      dependencies = "d3-hexjson-1.1.0/build/d3-hexjson.min.js",
    )
  })

  output$msg <- reactive({ input$geonm })
  output$tab <- renderTable({ data() })
}

shinyApp(ui = ui, server = server)



