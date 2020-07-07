# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    lat = 0.0
    lon = 0.0

    def __init__(self, lt, lg):
        self.lat = lt
        self.lon = lg

    def display(self):
        print("latitude is = " + str(self.lat))
        print('Longitude is = ' + str(self.lon))

obj = LatLon(44, 122)

obj.display()
    
        

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoints(LatLon):
    def __init__(self, name, lt, lg):
        self.name = name
        super().__init__(lt, lg)
    
    def __str__(self):
        return {'name':self.name, 'lt':self.lat, 'lg':self.lon}

    def display_waypoint(self):
        print('Name is = ' + str(self.name))
        print("latitude is = " + str(self.lat))
        print('Longitude is = ' + str(self.lon))
       

objw = Waypoints("Waypoint", 42, 100)
    
objw.display_waypoint()
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoints):
    def __init__(self, name, difficulty, size, lt, lg):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lt, lg)
    
    def display_geo(self):
        print('This is difficulty ' + str(self.difficulty))
        print('This is size ' + str(self.size))
        print('This is lat from geo ' + str(self.lat))
        print('This is lon from geo ' + str(self.lon))
    
objg = Geocache("Geo", "Hard", "Large", 28, 144)

objg.display_geo()

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoints("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE 
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache.__str__())
