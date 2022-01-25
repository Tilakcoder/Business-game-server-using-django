# Business-game-server-using-django
Hello everyone, This is a simple project which consists of real-time virtual money payment gateway. I made this program just to solve the change problems in money related board games.

# About-Project-Development
I have used django and channels (in-memory channels) to make this project. This project consists of Python, Html, CSS and Javascript languages. All the CSS and Javascript codes are inserted in HTML files only ,i.e, There is only in-page CSS and Javascript. In this project I have made two django apps named ``business`` and ``chat``. whole game is based on these two apps. Al the ``.html`` files are arranged in ``templates`` folder.

``chat`` app is used handle websocket connections and ``business`` app is used to manage all the data in the form of Django models.

# How-to-run-this-project
This project templates has responsive designs because there main use will be with the mobile phones. As we are going to use this app for virtual money transfer from mobile to mobile. So, we have to run this server program that can server pages to another devices in the network. For making it possible localhost ,i.e., ``127.0.0.1`` will not work for other devices you can just play among diffrent tabs of the browser only inside the system where the server is running.

So, For making the server live for other devices you need to know your IP address first and enter it in ``allowed_hosts`` lists in ``settings.py`` file. Run the below command to run the server:
``python manage.py runserver 'your-ip-address':8000``

# How-to-use-this-project
I tried to make it super simple to initiate a room and start playing. After making the server live Enter the site address in the browser of any device. Now enter the name as Bank and New ``Board`` name (room-name). If you entered a new Board name you will be reditrected to ``create`` page and set the intital amount of all players and Bank. After that this device will be your bank.

Now other players are ready to go. Ask all other players to type the same url. After that they have to enter their name which should be unique and ``Board name`` that you will tell them. You have tell the same Board name that you have entered.
