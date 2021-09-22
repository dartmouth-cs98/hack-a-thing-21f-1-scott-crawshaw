# Tee Time Notifier


## What you built? 

This Saturday, I have a golf tee time for 3:30pm. Unforuantely, that is later in the day than I would prefer, but there are no availible tee times before then. I suspect one will open up soon, but somebody may take it quickly. Therefore, in an effort to learn about webscraping and automated sms services, I built a tool to help me get a better tee time.  
  
I created a python script that scrapes the tee time website, checking to see if there is a tee time for 2 availible between 11am and 3:20pm on Saturday. If there is, it uses twilio to send an sms message to my phone, alerting me of the opening. The script is hosted in PythonAnywhere, a neat website that lets you schedule a script to run on a repeating interval. I set my script to run every 10 minutes, alerting me quickly if a tee time opens up. I've included screenshots of the text I will recieve if a tee time opens up, as well as the task scheduling in PythonAnywhere.

![Text Example](https://github.com/dartmouth-cs98/hack-a-thing-21f-1-scott-crawshaw/blob/main/Golf%20Scraping/text_example.png?raw=true "Text Example")  
![PythonAnywhere](https://github.com/dartmouth-cs98/hack-a-thing-21f-1-scott-crawshaw/blob/main/Golf%20Scraping/tasks.png?raw=true "PythonAnywhere")

## Who Did What?

Scott Crawshaw completed the project alone.

## What you learned

This project taught me a great deal about web scraping & twilio, two tools that may prove useful in future projects. I found that twilio was simple to setup and use, and that PythonAnywhere is an excellent place to host python scripts. I had used these tools lighly in the past, but this provided a much greater insight into how to apply these resources. This project was certianly quicker than the wifi one, but may very well be more applicable for the group project, as automated sms is a powerful tool.

## Authors

Scott Crawshaw

## Acknowledgments

To help with the twilio sms code, I used the following twilio tutorial https://www.twilio.com/docs/sms/quickstart/python.
