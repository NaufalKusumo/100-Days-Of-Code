capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

val = travel_log["Germany"]["cities_visited"][2]
nested_list = ["A", "B", ["C", "D"]]

print(val)