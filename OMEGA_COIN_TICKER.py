import os
import json
import urllib2
import time
from decimal import Decimal, ROUND_HALF_UP
from OmegaExpansion import oledExp

def write ():
    ### this gets the date and time
    date = time.strftime("%d %b %Y %H:%M")
    #time_now = time.strftime("%X")
    
    ### these are the API calls for the four currencies
    response_1 = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR')
    r_1 = json.load(response_1)
    
    response_2 = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/monero/?convert=EUR')
    r_2 = json.load(response_2)
    
    response_3 = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/iconomi/?convert=EUR')
    r_3 = json.load(response_3)
    
    response_4 = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/siacoin/?convert=EUR')
    r_4 = json.load(response_4)
    
    ### this sets a place value for the Decimal round up
    cents = Decimal('0.001')
    #cents2 = Decimal('0.0001')
    
    ### these set the JSON resturns to variables
    c_1 = r_1[0]
    c_2 = r_2[0]
    c_3 = r_3[0]
    c_4 = r_4[0]
    
    ### this grabs info from the dictionaries, and makes them variables
    c_1_sym = c_1['symbol']
    #c_1_price = round(float(c_1['price_eur']), 2)
    c_1_price = c_1['price_eur']
    c_1_price = Decimal(c_1_price).quantize(cents, ROUND_HALF_UP)
    c_1_per = c_1['percent_change_24h']
    
    c_2_sym = c_2['symbol']
    #c_2_price = round(float(c_2['price_eur']), 2)
    c_2_price = c_2['price_eur']
    c_2_price = Decimal(c_2_price).quantize(cents, ROUND_HALF_UP)
    c_2_per = c_2['percent_change_24h']
    
    c_3_sym = c_3['symbol']
    #c_3_price = round(float(c_3['price_eur']), 2)
    c_3_price = c_3['price_eur']
    c_3_price = Decimal(c_3_price).quantize(cents, ROUND_HALF_UP)
    c_3_per = c_3['percent_change_24h']
    
    c_4_sym = c_4['symbol']
    #c_3_price = round(float(c_3['price_eur']), 2)
    c_4_price = c_4['price_eur']
    c_4_price = Decimal(c_4_price).quantize(cents, ROUND_HALF_UP)
    c_4_per = c_4['percent_change_24h']
    
    ### this is the write to screen process
    if oledExp.driverInit() != 0:
        print 'ERROR: Could not initialize the OLED Expansion'
        return False
        
    ### this clears the screen
    oledExp.clear()
    
    ### this sets the colour
    oledExp.setDisplayMode(0)
    
    ### this sets it to receive text
    oledExp.setTextColumns()
    
    ### this places the cursor on the second row, first column
    oledExp.setCursor(1,0)
    
    ### oledExp.write('  '+date+' '+time_now)
    oledExp.write(date)
    
    oledExp.setCursor(3,0)
    oledExp.write(c_1_sym+': '+str(c_1_price)+' '+c_1_per+'%')
    
    oledExp.setCursor(4,0)
    oledExp.write(c_2_sym+': '+str(c_2_price)+'  '+c_2_per+'%')
    
    oledExp.setCursor(5,0)
    oledExp.write(c_3_sym+': '+str(c_3_price)+'   '+c_3_per+'%')
    
    oledExp.setCursor(6,0)
    oledExp.write(c_4_sym+':  '+str(c_4_price)+'  '+c_4_per+'%')
    
    ### this sets the scroll type, speed, etc 
    oledExp.scroll(0, 0, 0, 8-1)

### this calls the function
write()
    
    
    