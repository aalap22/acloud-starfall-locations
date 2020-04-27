import requests
#print(requests.get("http://nasa.gov"))

#resp = requests.get("http://bbc.com")
#print(resp)
#print(resp.status_code)
#print(resp.text)

#in this project we will find the nearest location for the metors / starfall from our current place.
# to do this we will first get list of location from NASA website.
# 2nd we will parse longitude and latitude of all locations
# compare the distance from your current location
# print top 10 sites to see starfall

starfall_resp = requests.get("https://data.nasa.gov/resource/gh4g-9sfh.json")
print(starfall_resp.status_code)
starfall_resp_json = starfall_resp.json()
#print(starfall_resp_json) # response

print(starfall_resp_json[1])
n = 0
for s in starfall_resp_json:
    n = n+1
print("Number of locations are: ", n)

print(type(starfall_resp_json)) # So starfall_resp_json is type list

#each item in the list is a dictionary

"""
for s in starfall_resp_json:
    print(type(s)) # you can see type for each item is dictionary
"""

my_lat = 37.520295
my_long = -121.994445
my_loc = (37.520295,-121.994445) # just put the value in tuple
starfall_lat = float(starfall_resp_json[1]["reclat"]) # convert result to float otherwise it will be in the form of string which won;t help
starfall_long = float(starfall_resp_json[1]["reclong"])
print(starfall_lat,starfall_long)

# now to calculate distance between two points on earth below is the formula
import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

print(calc_dist(starfall_lat,starfall_long,my_lat,my_long))
print(calc_dist(my_lat,my_long,starfall_lat,starfall_long))

dist = []
# now let's calculate it for all the sites
for site in starfall_resp_json:
    if "reclat" in site and "reclong" in site:
        site["distance"] = calc_dist(float(site["reclat"]),float(site["reclong"]),my_lat,my_long)
        dist.append(site["distance"])
    else:
        continue

print(starfall_resp_json[0]) # now you can see distance field is added to starfall_distance_json
print(type(starfall_resp_json[0]["distance"])) # distance is in float. Perfect.
print(dist[0:10])

dist.sort()
print(dist[0:10])
#dist = []
#next is sort the distance to have lesser to higher distance
#for site in starfall_resp_json:
 #   dist = dist.append(starfall_resp_json.g
