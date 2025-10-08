# K-Line-Chart-by-Pygame
You just need to record the prices of something at different times, and you can see its candlestick chart. The program uses Pygame and is not very large overall.

Manual
Ensure the project structure is as follows:
  dir
    DATA
      thingName
        input.txt
        history.txt
      graph.json
    main.py
    graphRender.py
    option.txt
Record the price in input.txt, using ',' to separate different times of the day and ';' to separate different days. In history.txt, add purchase records, using ';' to separate batches, with the left of ',' being the trade volume and the right being the trade price. In option.txt, the left of ',' is the selected folder, and the right is the ratio of the price in the image to the grid length.
