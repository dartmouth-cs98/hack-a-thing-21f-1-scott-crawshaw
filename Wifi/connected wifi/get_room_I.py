from subprocess import check_output
import jc.parsers.airport as airport
import sqlite3
import sys

# adapted from https://www.sqlitetutorial.net/sqlite-python/creating-database/
def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect("wifi_aps_i.db")
        cursor = conn.cursor()
        return cursor
    except sqlite3.Error as e:
        sys.exit(e)

def get_ap_id():
    output = check_output(["airport", "-I"]).decode('UTF-8')
    nearest_ap = airport.parse(output)
    if "bssid" in nearest_ap:
        return nearest_ap["bssid"][:-3]
    else:
        sys.exit("No wifi found.")

# adapted from https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
def print_ap(cursor):
    bssid = get_ap_id()
    if len(bssid) > 0:
        try:
            cursor.execute("SELECT name FROM wifi WHERE bssid=?;", (bssid,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                print(rows[0][0])
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