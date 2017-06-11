# crypto-ticker

This is a crypto-ticker for the omega-onion

There are some files and explanation to follow. 

This program allow the omega to utilise the coinmarket cap API. At the moment it displays four cryptocurrnecies, their ticker, current EUR price, and the % change for the last 24 hours. 

Updates to follow

### Some updates here

### this must be added to etc/crontabs. It runs the script every three minutes (every minute that is divisible by three)

*/3 * * * * python /root/btc-flash/btcFlash.py
#

### this must be added to the /etc/rc.local It loads the program on startup. Remember that the correct permissions must be given to the script. This command is below

# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

python /root/btc-flash/oled-start.py

sleep 8

python /root/btc-flash/btcFlash.py

exit 0


### this is the command to give the correct permissions to the script once it is placed in the root folder. 

chmod +x /root/btc-flash/oled-start.py

chmod +x /root/btc-flash/btcFlash.py