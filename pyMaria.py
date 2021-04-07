import mariadb
import sys
import time

filename = time.strftime("%Y-%m-%d")

temp1 = 25
temp2 = 30

hum1 = 40
hum2 = 90

totTemp = (temp1 + temp2) / 2
totHum = (hum1 + hum2) / 2

hours = 1
#//////////////////////////////DB\\\\\\\\\\\\\\\\\\\\\\\\\

try:
    con = mariadb.connect(
        user="",
        passwd="",
        host="",
        port=,
        database="",
        )
        
except mariadb.Error as e:
        print(f"Error connecting to mariaDB Platform: {e}")
        sys.exit(1)
        
cur = con.cursor()

cur.execute("INSERT INTO oven1 (date, temp, humid, hours_running) VALUES (%s, %d, %d, %d)",("Nani", totTemp, totHum, hours))

con.commit()

print("Record is inserted...")