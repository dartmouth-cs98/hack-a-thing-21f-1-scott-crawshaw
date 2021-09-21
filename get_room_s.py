from subprocess import check_output
import jc.parsers.airport_s as airport
import sqlite3
import sys

# adapted from https://www.sqlitetutorial.net/sqlite-python/creating-database/
def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect("wifi_aps_s.db")
        cursor = conn.cursor()
        return cursor
    except sqlite3.Error as e:
        sys.exit(e)

def get_ap_id():
    output = check_output(["airport", "-s"]).decode('UTF-8')
    access_points = airport.parse(output)
    sorted_points = sorted(access_points, key=lambda o: o['rssi'], reverse=True)
    nearest_ap = list(filter(lambda o: o["ssid"]=="eduroam",sorted_points))[0]
    return nearest_ap["bssid"][:-3]

def print_ap(cursor):
    bssid = get_ap_id()
    if len(bssid) > 0:
        try:
            cursor.execute("SELECT name FROM wifi WHERE bssid=?;", (bssid,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                print(rows[0])
            else:
                print("Cannot determine location. Please try again.")
        except sqlite3.Error as e:
            print(e)
    else:
        print("Could not locate wifi access point. Please try again.")

cursor = create_connection()
while True:
    name = input("Hit enter to get name of room. ")
    print_ap(cursor)