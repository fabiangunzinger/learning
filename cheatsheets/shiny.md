# Shiny cheatsheet


- Outputs are recipes. We tell shiny *how* to do something, not *when* to do something. Examples: `output$plot <- renderPlot(...)` is a recipe that tells shiny how to update plot when it's necessary (good), `observe({ output$plot <- renderPlot(...)` is a directive to shiny to update the plot whenever `...` changes, which is a fundamental misunderstanding of how outputs work.

- A reactive expression produces a value (e.g. single value or dataframe), and
    is reactive to all its reactive components. 

- Prefer reactive expressions to model calculations over using observers to set
    reactive variables.

- Invisible outputs (e.g. in a hidden tab) are suspended and reactive values
    that feed into it won't be updated.

- Think about one goal of shiny programming as producing as many outputs as
    possible (all that are needed) while running as few of the intermediary
    elements (reactive expressions) as possible.

- Observers force shiny to run code, it's the anti-pattern to the first
    point: we tell Shiny when to do that, rather than just how to do a thing.
