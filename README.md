## Meraki Captive Portal / Splash Page for Telcel

This program simulates a splash page captive portal for users that want to connect to a Meraki access point for the first time. Upon initial connection, users are redirected to a splash page that prompts for a phone number and email address. When these fields are filled out, the user is allotted 30 minutes to browse the web. When those 30 minutes are completed (assuming the splash frequency is set to 30 minutes on the Meraki dashboard for the access point), the user is redirected to another splash page, where they must sign in using their Facebook credentials in order to use the internet for an additional 30 minutes.

In order to run this in your environment, follow these steps:

```
$ cd meraki-captive-portal/sample-captive-portal

```

```
$ python3 meraki_captive_portal.py

```

Now go to your browser and enter http://localhost:5004/click - this will take you to the splash page where the user can enter in their phone number and email address.

Once the information has been inputted, hitting Register will give a success screen that notifies the user that they have 30 minutes to continue browsing.

If you enter http://localhost:5004/click at this point, you will see that the splash page changes and asks for the user to enter their Facebook credentials.

Once again, the user will have an additional 30 minutes to browse the web once the information has been submitted.

If you would like to see where the user's information is stored (phone number, email address, whether he/she logged in through Facebook):
```
$ vi userInfo.txt

```

