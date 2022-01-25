# Business-game-server-using-django
Hello everyone, This is a simple project which consists of real-time virtual money payment gateway. I made this program just to solve the change problems in money related board games.

# About-Project-Development
I have used django and channels (in-memory channels) to make this project. This project consists of Python, Html, CSS and Javascript languages. All the CSS and Javascript codes are inserted in HTML files only ,i.e, There is only in-page CSS and Javascript. In this project I have mad eteo django apps named ``business`` and ``chat``. whole game is based on these two apps. Al the ``.html`` files are arranged in ``templates`` folder.

``chat`` app is used handle websocket connections and ``business`` app is used to manage all the data in the form of Django models.

# How-to-run-this-project
This project templates has responsive designs because there main use will be with the mobile phones. As we are going to use this app for virtual money transfer from mobile to mobile. So, we have to run this server program that can server pages to another devices in the network. For making it possible localhost ,i.e., ``127.0.0.1`` will not work for other devices you can just play among diffrent tabs of the browser only inside the system where the server is running.

So, For making the server live for other devices you need to know your IP address first and enter it in ``allowed_hosts`` lists in ``settings.py`` file. Now activate the virtual environment and run the below command to run the server:
``python manage.py runserver 'your-ip-address':8000``
