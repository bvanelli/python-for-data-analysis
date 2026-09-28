# Assignment 13 — Concepts of Clean Code

In our recap, we've seen how to analyze an airport dataset. In daily tasks, we will use simple scripts like 
the following, to do a quick-check on a dataset quickly.

This one runs through the airport dataset, calculates the distance of every airport to every other airport 
(after filtering by medium or large airport), then displays **the most remote airport**. This is defined
as the airport whose closest neighbour is farther away than for any other airport.

```python
import pandas as pd
import math

df = pd.read_csv("../data/flights/airports.csv")

# go through all the airports and keep the ones we want
lats=[]
lons = []
names = []
idents=[]
for i in range(len(df)):
    t = df["type"].iloc[i]
    # only keep the large and medium airports
    if t=="large_airport" or t == "medium_airport":
        lats.append(df["latitude_deg"].iloc[i])
        lons.append( df["longitude_deg"].iloc[i] )
        names.append(df["name"].iloc[i])
        idents.append( df["ident"].iloc[i])

# now find the most remote airport in the world (furthest from any other)
best=None
bestdist = 0
for i in range(len(lats)):
    near = 999999999
    nearj = -1
    for j in range(len(lats)):
        # do not compare an airport with itself
        if i != j:
            lat1=lats[i]
            lon1 = lons[i]
            lat2 = lats[j]
            lon2=lons[j]
            # only use it when the coordinates are there
            if lat1 != None and lat2 != None:
                # calculate radians to compute total distance
                r1 = lat1*3.141592653589793/180
                r2 = lat2 * 3.141592653589793 / 180
                d1=(lat2-lat1)*3.141592653589793/180
                d2 = (lon2 - lon1) * 3.141592653589793 / 180
                # See Haversine formula: https://en.wikipedia.org/wiki/Haversine_formula
                x = math.sin(d1/2)*math.sin(d1/2)+math.cos(r1)*math.cos(r2)*math.sin(d2/2)*math.sin(d2/2)
                dist=2*6371.2*math.asin(math.sqrt(x))
                # keep the closest airport we have seen so far
                if dist<near:
                    near = dist
                    nearj = j
    if near>bestdist:
        bestdist = near
        best=i
        # we just found an airport more remote than any before it
        print("new most remote so far: "+names[i]+" -> closest is "+names[nearj]+" ("+str(round(near))+" km)")

print("The most remote airport in the world is " + names[best] + " (" + idents[best] + ")")
print("The closest airport to it is " + str(round(bestdist)) + " km away")
```

Even though this code works, it is very hard (painful) to read and to maintain. Imagine the pain of having to change
the code to find the two _closest_ airports!

Follow the steps below to refactor this script to something more manageable. Remember that **your steps should be
_very_ small**: you change one thing, test if nothing broke, then iterate again.

Before changing anything, run the script once and save its output: this is your reference. After every step, the
**output must stay the same**. For reference, the script should find _Mataveri International Airport (SCIP)_.

## Replace the loader and main

1. Refactor the script to contain an entrypoint. Nothing should be global, and it should follow the template:

   ```python
   def main() -> None:
       ...

   if __name__ == '__main__':
       main()
   ```

2. Refactor the data loading. You want a **function** to load the data that looks like this:
   `airports = load_airports("../data/flights/airports.csv", size_filter=["large_airport", "medium_airport"])`,
   returning a `DataFrame`.

## Use `dataclasses` for data storage

1. Create a frozen dataclass `Location(ident: str, name: str, latitude: float, longitude: float)` to store your airport
   data.
2. Wire the new dataclass into the program, ensuring the new attributes are being used.
3. Create a method `def distance(self, other: "Location") -> float:` for your dataclass, to generalize the distance
   calculation between airports.
4. Two airports are the same airport if they share the same `ident`. Make sure that two `Location` objects are equal
   when their `ident` matches, regardless of the other attributes. **Hint**: look at the `__eq__` dunder method.
5. Add unit tests for your new code, and execute them. If they fail, look at your code if something is wrong.

   ```python
   def test_distance():
       """Example taken from https://en.wikipedia.org/wiki/Haversine_formula"""
       white_house = Location("WH", "White House", 38.898, -77.037)
       eiffel_tower = Location("ET", "Eiffel Tower", 48.858, 2.294)
       distance = white_house.distance(eiffel_tower)
       assert round(distance, 1) == 6161.6

   def test_equality():
       """Two locations are the same airport when their ident matches"""
       frankfurt = Location("EDDF", "Frankfurt am Main Airport", 50.033, 8.570)
       frankfurt_renamed = Location("EDDF", "Frankfurt Airport", 50.030, 8.560)
       munich = Location("EDDM", "Munich Airport", 48.354, 11.786)
       assert frankfurt == frankfurt_renamed
       assert frankfurt != munich
   ```

**Hint:** you might want to look at the documentation for
[pytest](https://docs.pytest.org/en/stable/getting-started.html).

## Wrap it together

1. Write a function for the nearest neighbour using the bruteforce approach. Here is a hint for the
   function signature: `def nearest_neighbour(origin: Location, locations: list[Location]) -> tuple[Location, float]:`
2. Wrap the whole evaluation loop to use your new function, then run the script to find the same result.
3. Benchmark: did your script improve its performance? Find the performance hotspots, and see if you can optimize them.

## **Bonus Assignment**: AI assisted refactoring

Use a harness of your choice (Claude Code, Codex, Gemini CLI, OpenCode) and use it to refactor the same code snippet
above. Watch what the harness does and steer it in the right direction. Can you balance refactoring speed with
readability? The goal here is to speed the refactoring while being in control of the design choices.
