
import json
infile = open("eq_data.json","r")
data = json.load(infile)
print("The total number of earrhquakes is:", data["metadata"]["count"])
print()


eq_dict = {}

for feature in data["features"]:
   if feature["properties"]["mag"] > 6:
      location = feature["properties"]["place"]
      magnitude = feature["properties"]["mag"]
      longitude = feature["geometry"]["coordinates"][0]
      latitude = feature["geometry"]["coordinates"][1]

      eq_dict[location]= {"location": location, "magnitude": magnitude, "longitude": longitude, "latitude": latitude}

print(eq_dict)
print()


for key,value in eq_dict.items():
   print("Location:", key)
   print("Magnitude:", value["magnitude"])
   print("Longitude:", value["longitude"])
   print("Longitude:", value["latitude"])
   print()
   print()


   
