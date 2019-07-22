library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
    #ui-components:
    sliderInput(inputId = "slide", label = "lblSlider", min = 0, max = 100, value = 73, width = 2000),
    plotOutput("plot")
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    #(server) functions
    output$plot <- renderPlot({
        title <- "title"
        hist(
            rnorm(input$slide), col = "#662222"
            )
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
