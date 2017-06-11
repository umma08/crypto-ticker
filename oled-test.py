from OmegaExpansion import oledExp
from time import localtime, strftime

date = strftime("%d %b %Y %H:%M", localtime())

# this clears the screen
oledExp.clear()
    
# this sets the colour
oledExp.setDisplayMode(0)
    
#this sets it to receive text
oledExp.setTextColumns()
    
#this places the cursor on the second row, first column
oledExp.setCursor(1,0)

#this writes the time and date
oledExp.write(date)
    
# first json response printed
#oledExp.setCursor(3,0)
#oledExp.write(c_1_sym+': '+str(c_1_price)+' '+c_1_per+'%')