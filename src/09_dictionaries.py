"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

from pprint import pprint

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({
    "lat": 42,
    "lon": -120,
    "name": "the good place"
})

pprint(waypoints)
print('\n-------------------\n')

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
desiredPlace = 0

# update desiredPlace with index of dictionary in list "waypoints" that has a key "name" with the value "a place"
for i, place in enumerate(waypoints):
    if place["name"] == "a place":
        desiredPlace = i

waypoints[desiredPlace].update({
    "lon": -130
})

pprint(waypoints)
print('\n-------------------\n')


# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for i, place in enumerate(waypoints):
    placeKeys = place.keys()
    print(f"waypoint index: {i}")

    for daKey in placeKeys:
        print(place[daKey])
    
    print('\n~~~~~~~~~~~~~~~\n')