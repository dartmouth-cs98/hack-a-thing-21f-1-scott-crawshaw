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
        cursor.execute("CREATE TABLE IF NOT EXISTS wifi (bssid text PRIMARY KEY, name text);")
        conn.commit()
        return conn, cursor
    except sqlite3.Error as e:
        sys.exit(e)

def get_ap_id():
    output = check_output(["airport", "-I"]).decode('UTF-8')
    nearest_ap = airport.parse(output)
    if "bssid" in nearest_ap:
        return nearest_ap["bssid"][:-3]
    else:
        sys.exit("No wifi found.")

# adapted from https://www.sqlitetutorial.net/sqlite-python/insert/
def insert_ap(name, conn, cursor):
    bssid = get_ap_id()
    if len(bssid) > 0:
        try:
            cursor.execute("INSERT INTO wifi (bssid, name) VALUES (?,?);", (bssid, name))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
    else:
        print("Could not locate wifi access point. Please try again.")
    
conn, cursor = create_connection()
while True:
    name = input("Name of current room: ")
    insert_ap(name, conn, cursor)


