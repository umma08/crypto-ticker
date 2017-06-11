import os
from OmegaExpansion import oledExp

def start_write ():
	if oledExp.driverInit() != 0:
		print 'ERROR: Could not initialize the OLED Expansion'
		return False
        
        # this clears the screen
        oledExp.clear()
        
        # this sets the colour
        oledExp.setDisplayMode(0)
        
        #this sets it to receive text
        oledExp.setTextColumns()
        
        #this places the cursor on the second row, first column
        oledExp.setCursor(1,0)
        
        oledExp.write('Welcome.')
        
        oledExp.setCursor(3,0)
        
        oledExp.write('Loading ticker..')
        
        oledExp.setCursor(5,0)
        
        oledExp.write('Prices in EUR.')
       
start_write()

