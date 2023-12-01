import requests

# See README.md
cookie = ""

# this will get the data from the server, returning a RequestObject, 
# which has a .text property we read the content out of, which is returned.
def get_day_data(daynumber):
    return requests.get(f"https://adventofcode.com/2023/day/{daynumber}/input", cookies={"session":cookie}).text
