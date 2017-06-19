# crypto-ticker

This is a crypto-ticker for the OmegaOnion

There are some files and explanations to follow in more detail, with respect to setting up the OmegaOnion. 

The program allow the Omega to utilise the Coinmarket Cap API. At the moment it displays four cryptocurrnecies, their ticker symbol, current EUR price, and the % change for the last 24 hours. 

## /etc/crontabs

The following line this must be added to /etc/crontabs. 

It runs the script every three minutes (every minute that is divisible by three)

*/3 * * * * python /root/btc-flash/btcFlash.py

Ensure that a # follows the command on the line below in the crontabs file. 
Otherwise it will not run

## /etc/rc.local 

The following commands must be placed in this file. It loads the program on startup. 

python /root/btc-flash/oled-start.py

sleep 8

python /root/btc-flash/btcFlash.py

exit 0

Remember that the correct permissions must be given to the script. 

These commands are seen below this section

## setting correct permissions

chmod +x /root/btc-flash/oled-start.py

chmod +x /root/btc-flash/btcFlash.py