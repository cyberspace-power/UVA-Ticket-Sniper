import pyautogui
import smtplib
from scapy.all import *

# ----------EDIT ME----------
MY_PHONE_NUMBER = "1234567890"  # Replace with your phone number with NO DASHES OR SPECIAL CHARACTERS
MY_PHONE_CARRIER = "verizon? att? EDIT ME"  # Replace with your carrier (Choose att, tmobile, verizon, or sprint)
MY_EMAIL_ADDRESS = "editme.........@gmail.com"  # Replace with your email address you want the message to come from
MY_EMAIL_ADDR_PASSWORD = "EDIT ME"  # Replace with your email address account password
# ---------------------------

carriers = {
    'att': '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com'
}

IS_WEBPAGE_CHANGE = False  # This is true when after the right clicks the webpage changes as intended


def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = (MY_PHONE_NUMBER + '{}').format(carriers[MY_PHONE_CARRIER])
    auth = (MY_EMAIL_ADDRESS, MY_EMAIL_ADDR_PASSWORD)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)


def setup_mouse():
    print("Currently on the UVA ticketing website, once you are logged in and navigated to the appropriate webpage, it"
          " should take 3 clicks to check if a ticket is available:")
    print("Click 1: You need to click on the plus button to increase your ticket quantity from 0 to 1")
    print('Click 2: You need to click "Add to Cart"')
    print("Click 3: Assuming a ticket was not found, you will have to click on the link on the word 'here' to return to"
          " the previous page to try again")
    print("This function will setup what mouse position the sniper will need to click for each of these three clicks.")
    print("\n--------------------DIRECTIONS--------------------\n"
          "Step 1: Place your web browser in the position you will want to leave it for the duration of "
          "your sniping session (If it moves, the mouse will click in the wrong place).\nStep 2: When prompted for each"
          " of the three clicks, move your mouse to the appropriate place on the screen in order to make the "
          "corresponding click happen\nStep 3: Press <ENTER> when you have positioned your cursor properly.\nStep 4: "
          "Repeat this process for each of the 3 clicks\nStep 5: You will also be asked to provide a 4th click. Place "
          "your cursor at the top bar of this window and press <ENTER>.\n\tThis is necessary because when the sniper is"
          " running, it will be hard to exit the program")
    print("*NOTE: Make sure when you position your mouse that you leave this window active so it can register your key "
          "press")
    print("*NOTE2: Make sure this window is always visible so the 4th click clicks on this window to allow you to exit"
          " if you want to.\n\nYOU CAN EXIT THIS PROGRAM BY TYPING <CTRL> + C WHILE THIS WINDOW IS ACTIVE\n")
    click_pos_list = []
    for i in range(4):
        time.sleep(1)
        input("Position your cursor for click " + str(i + 1) + " now. Press <ENTER> to capture the position...")
        coords = pyautogui.position()
        click_pos_list.append(coords)
    print(click_pos_list)
    return click_pos_list


def pkt_callback(pkt):
    global IS_WEBPAGE_CHANGE
    IS_WEBPAGE_CHANGE = True
    # pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}")


# Refractored function that happens within while True loop in snipe function
def snipe_helper(click_loc):
    global IS_WEBPAGE_CHANGE
    for i in range(len(click_loc)):
        # If your internet is slower, increse the first argument in random.gauss (number of average seconds) as needed.
        pyautogui.moveTo(click_loc[i][0], click_loc[i][1], random.gauss(5, 1), pyautogui.easeOutQuad)
        # Before making next click, ensure that the webpage changed after the 2nd or 3rd click
        if i == 2:
            IS_WEBPAGE_CHANGE = False
        if i == 3:
            if IS_WEBPAGE_CHANGE:
                IS_WEBPAGE_CHANGE = False
            else:
                send("TICKET SNIPED!!!")  # Ticket found! Terminate
                return False  # Ticket has been found, terminate loop in sniper function

        pyautogui.click()
    return True  # Need to continue looping


def snipe(click_loc):
    time.sleep(4)
    sniffer.start()
    continue_loop = True
    while continue_loop:
        continue_loop = snipe_helper(click_loc)  # Refractor function
    sniffer.stop()


sniffer = AsyncSniffer(filter='tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0 and ip host 216.177.87.229',
                       prn=pkt_callback, count=0, store=False)
clicks = setup_mouse()
snipe(clicks)
