import airport

# Airport code adapted from https://pypi.org/project/airport-py/
print(airport.info())
scan_results = airport.scan()
print(map(lambda r: (r.ssid, r.bssid, r.channel), scan_results[:3]))