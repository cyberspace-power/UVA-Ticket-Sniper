PURPOSE: 
Never get left out of a UVA basketball game again! Yeah, you got screwed. You didn't get the group 1 ticket to the Duke game you wanted, and you don't want to waste your time clicking over and over and over again trying to get a group 8 ticket to the game. Fear not! This tool will snipe a group 8 ticket for you! All you have to do is let it run on your computer and wait for a text telling you that your ticket has been sniped! You will then have around 5 minutes to confirm the ticket sale and walk away ready for the game!

SYSTEM REQUIREMENTS: 
The code was tested on Windows, but it should work on any OS.
You will need to download the following:
* Python 3.10+ -- https://www.python.org/downloads/release/python-3100/
	- Make sure you add Python and the Python Scripts folder to your PATH variable. There might be an option to do this when you download Python for the first time, but if you forgot are aren't sure if you added it, check out this link for help for windows -- https://geek-university.com/python/add-python-to-the-windows-path/

* After Python 3.10 is installed, you may need to install 2 package dependencies. You can do this by simply typing the following commands into your terminal (command prompt/powershell for windows):
	- pyautogui: Run this--> pip3 install pyautogui
	- scapy: Run this --> pip3 install scapy
		^ If these commands don't work, try typing "pip" instead of "pip3"

DIRECTIONS:
* Step 0: Create a dummy email address. I highly recommend creating a new dummy email address for the sole purpose of texting your phone with this app. The reason is that in the next step, we will be changing a google account setting which might make your account insecure.

* Step 1: While logged into your (dummy or not) email google account, navigate to the following link -- https://myaccount.google.com/lesssecureapps -- Turn this setting ON. You may exit out once done.

* Step 2: You need to change the global variables at the top of the python script named "sniper.py". Open the file in notepad or any other word processor of your choosing. Edit the following 4 variables:
	1. MY_PHONE_NUMBER
		- Put your cell phone number inside the quotation marks. This is the phone number that will be texted when a ticket is sniped. Enter your phone number in 9 digit format (i.e. "1234567890")
	2. MY_PHONE_CARRIER
		- Put your cell phone carrier. This is necessary so the texting works properly. (Your text will come from an email address of yours or a new one you set up.) You may choose from "verizon", "tmobile", "att", or "sprint"
	3. MY_EMAIL_ADDRESS
		- Put your email address that you want to text your phone number with. A few notes:
			^ This MUST be a GMail account (Your UVA email should work until they switch to Office 365 next year)
	4. MY_EMAIL_ADDR_PASSWORD
		- Put your gmail account password here

* Step 3: Open a terminal (cmd or powershell for windows)

* Step 4: Navigate to the webpage corresponding to the game who's ticket you are trying to snipe. 
	- Login to your UVA shots account
	- Navigate to the game page of the game who's ticket you want to snipe. This should be the page where you see at least 1 (usually 2) plus sign buttons indicating an increase in quantity, and an "add to cart" button below that.

* Step 5: Setting up your screen
	- You will need to organize your screen such that each of the buttons the sniper needs to click on is accessible. For instance, if you have a small screen, you will need to zoom out on your browser so you can see the "add to cart" button if you cannot see it. This program CAN NOT SCROLL. 
	- Additionally, you MUST make sure that your terminal is visible AT ALL TIMES, even when the program is clicking on the browser. If you do not do this, you WILL NOT BE ABLE TO STOP THE CODE without putting your computer into sleep mode or restarting. The mouse cursor is moving in an infinite loop, and you cannot stop it unless the terminal is visible. You will see why later.

* Step 6: Running the program
	- Make sure you have navigated to the folder where "sniper.py" is located in your terminal (Look up the change directory (cd) command for your OS if you do not know how to do this)
	- Run the script by typing one the following in your terminal. If one doesn't work, try a different variant. One of them will work.
		^ py sniper.py
		^ python sniper.py
		^ python3 sniper.py

* Step 7: Setting up the clicks
	- The first thing the code does is ask you to hover on various parts of the screen corresponding to the buttons that need to be pressed. When you hover over the appropriate spot, press <ENTER> to register the mouse position. Note that the mouse position can only be registerd if the TERMINAL IS ACTIVE. This means that the last thing you clicked on or interacted with was the terminal, not the webpage. If you click on the webpage, then hover the appropriate button and press enter, it won't work. Make sure before you press enter that you clicked on your terminal to make it active. You will need to input 4 different mouse positions:
		Position 1: Hover on the plus button to increase your ticket quantity from 0 to 1 (Ensure you are hovering over the correct plus sign -- you don't want to buy a student guest ticket)
		Position 2: Hover over "Add to Cart"
		Position 3: Assuming a ticket was not found, hover on the link on the word 'here' to return to the previous page to try again
		Position 4: Hover anywhere over your TERMINAL (more on this in a moment)

* Step 8: Kick back, and grab a beer
	- The code will be active until a ticket is found or you stop it (or it encounters an error)

* Step 9: Manually terminating the program
	- If you want to stop the program from running, wait until the 4th click in the cycle (corresponding to position 4 described above). This click will make the terminal active (this is why the terminal must be visible at all times). As soon as the terminal is activated, type the following key-press: <CTRL> + C -- This will terminate the program


OUTPUT: 
If everything works and a ticket is sniped, you should receive a text message saying "Ticket sniped!". You then will have around ~5 minutes to go online and complete the transaction. Otherwise, the code encountered an error

DEBUGGING: 
If your code is not working, there are a number of reasons this could be happening:
* Check steps 1-2 again. Make sure you followed those steps. In particular, double check your spelling in step 2
* Code stopped running, but I didn't receive a text, or I received a text, but did not get a ticket.
	- There are a number of reasons this could happen. But here are the two most likely:
		1. Your webpage took too long to load. The clicks happen in around a 5 second cycle. In other words, there is a new click every 5 seconds. If the webpage does not load quickly enough, the code will think that there is no link where it tried to click, and that it has found a ticket.
			^ You can fix this by taking the following action: Open "sniper.py" and navigate to line 77 (You can search (<CTRL> + F) for "pyautogui.moveTo", which should pull up this line). In this line, increase the first argument in the "random.gauss" function. That number corresponds to how long the code will take on average between clicks. The higher the number, the longer the webpage will have to load, and the smaller the chances of your code failing are.
		2. A ticket was sniped, but I missed the deadline because the text took too long or didn't arrive at all
			^ I am not sure exactly how to fix this. It worked when I tested my code with verizon's @vtext system... most of the time. Sometimes the text would take 10-15 to arrive to my phone. Additionally, it is possible if you have a different phone carrier that it will not work at all. I cannot test for other phone carriers.

		3. Something else? 
			^ Let me know if anything else is going wrong so I can fix it.