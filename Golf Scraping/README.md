# Tee Time Notifier


## What you built? 

This Saturday, I have a golf tee time for 3:30pm. Unforuantely, that is later in the day than I would prefer, but there are no availible tee times before then. I suspect one will open up soon, but somebody may take it quickly. Therefore, in an effort to learn about webscraping and automated sms services, I built a tool to help me get a better tee time.  
  
I created a python script that scrapes the tee time website, checking to see if there is a tee time for 2 availible between 11am and 3:20pm on Saturday. If there is, it uses twilio to send an sms message to my phone, alerting me of the opening. The script is hosted in PythonAnywhere, a neat website that lets you schedule a script to run on a repeating interval. I set my script to run every 10 minutes, alerting me quickly if a tee time opens up. I've included screenshots of the text I will recieve if a tee time opens up, as well as the task scheduling in PythonAnywhere.

![Text Example](https://github.com/dartmouth-cs98/hack-a-thing-21f-1-scott-crawshaw/blob/main/Golf%20Scraping/text_example.png?raw=true "Text Example")  
![PythonAnywhere](https://github.com/dartmouth-cs98/hack-a-thing-21f-1-scott-crawshaw/blob/main/Golf%20Scraping/tasks.png?raw=true "PythonAnywhere")

## Who Did What?

TODO: who worked on what part?

## What you learned

TODO: what worked / what didn't work

## Authors

TODO: list of authors

## Acknowledgments

TODO: cite any tutorials followed here
