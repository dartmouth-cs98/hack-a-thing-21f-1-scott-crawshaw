# Wifi Locator

## What you built? 

I built a python script that allows one to create a wifi map, and then use that wifi map to determine their current location. Basically, the user walks from room to room, giving the script the name of each room when they are in it. The script then grabs the nearest wifi access point's BSSID using the Mac airport tool, and stores it in a sql table with the room name. Once a sufficent number of rooms are mapped, the user can then go back to rooms, asking the script to guess which room they are in. By assessing the BSSID of the nearby wifi access point, the script attempts to recognize the location of the user.  
  
I built two seperate versions of this tool. One uses airport -s to scan all nearby wifi access points, determining the nearest one based on which has the strongest signal. The other uses airport -I to get the BSSID of the access point that the user is currently connected to. Both options seemed to provide similar degrees of efffectiveness, but the airport -s was significantly slower. On the flip side, the airport -s option doesn't require the user to be connected to wifi, where the airport -I option does.

## Who Did What?

Scott Crawshaw completed the project alone.

## What you learned

I attempted this project because of its possible use in one of my app ideas. Essentially, I would like to make an app that functions like apple's Find My Friends, but rather than providing a dot on a map, it provides the name of the room the user is in. This would only work at Dartmouth, where each room has a wifi access point, so the app could simply determine the BSSID of the nearest access point and reference a table to convert it to a name.  
  
Unfortunately, the tool did not work as well as I would hope. I tested it in both the library and the LSC, and both resulted in a subpar outcome. It sometimes produced the correct result, but often, the access point my computer was connected to would vary each time I entered a room. On the bright side, it does provide a relatively good estimate of the user's location, even if it gets mixed up between two adjacent rooms. A test of the app using 3 LSC rooms can be seen below.

![Wifi Scan Example](https://github.com/dartmouth-cs98/hack-a-thing-21f-1-scott-crawshaw/blob/main/Wifi/scan%20wifi/wifi_scan_test.png?raw=true "Wifi Scanning Example")  
![Connected Wifi Example](https://github.com/dartmouth-cs98/hack-a-thing-21f-1-scott-crawshaw/blob/main/Wifi/connected%20wifi/connected_wifi_test.png?raw=true "Connected Wifi Example")

## Authors

Scott Crawshaw

## Acknowledgments

Various websites were consulted for small snippets of code. When relevant, they are cited in the code. I've also included a list below.  
https://www.sqlitetutorial.net/sqlite-python/creating-database/  
https://www.sqlitetutorial.net/sqlite-python/insert/  
https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/  
https://stackoverflow.com/questions/26924812/python-sort-list-of-json-by-value
