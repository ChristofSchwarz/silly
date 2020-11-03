# The Ministry of Silly Charts
![screenshot](111f5604-7194-4123-9f02-e8ac19ff36f4_200x200.png "screenshot")<br> 
It is November again, time to make some real fun with Qlik Sense charts. In analogy of what the great Monty Pythons did to walk styles in their "Ministry of Silly Walks", basically I do to data visualizations here. Here I'm presenting this together with my daughter in this colorful fun video!

 - 2020 https://youtu.be/bBOv334Efcc
 
Included in 2020: The PacMan Chart, the Minecraft Chart, the Tetris Chart, the Empire State Chart, the Country Lane Chart, the London Bridge Chart, 
the Earth Rotation Chart, The Spiderweb Chart, the "Kranz" Chart, the Mandelbrot Chart, and the Qlik Guru Picture.

The app shown in the video is attached here as .zip (unzip first then import in QMC or export to `My Documents\Qlik\Sense\Apps`)

 ## Things you can paint when you are bored 
 With the help of the `ValueLoop(...)` or `ValueList(...)` formulas a chart can spin up a dimensionality without data being loaded before. Try it out:
 
 ### The PacMan Chart
 
 Start a new Pie Chart by dragging and dropping the pie chart symbol to the sheet.
  - As Dimension put this formula `=ValueLoop(1,2)'
  - Add a 1st Measure `=RowNo()-.5` which will drive the portion of the pie in the ratio 0.5 and 1.5, turning into 90° and 270°
  - Add a 2nd Measure `=RowNo()-.7` which will drive the size of the slice, the first one being much smaller, like 0.3 : 1.3
  - Down at the Appearance accordion section, find Colors and put "By Expression"
  - use this color formula `=Pick(RowNo(),Null(),'#FEFB00')` which will give the small segment a default color and the 2nd segment a yellow color
  - Under "Presentation" go to the advanced Styling and add a Large Outline width in White, so that the segments do not meet each other
  
 ### The Spider Web Chart
 
 
 ## Earlier versions
 
 - 2019 https://www.youtube.com/watch?v=risl1RTplzw
 - <img src="mosc2019.png" width="350">
