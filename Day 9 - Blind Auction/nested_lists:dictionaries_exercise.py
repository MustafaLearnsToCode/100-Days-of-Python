capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
}

# travel_log = {
#     "France": ["Paris","Marseille"],
#     "India": ["Bombay", "Indore", "New Delhi"],
# }

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "times_visited": 8,
        "cities_visited": ["Paris","Marseille"],
    },
    "India": {
        "times_visited": 10,
        "cities_visited":["Bombay", "Indore", "New Delhi"],
    },
}

print(travel_log["India"]["cities_visited"][1])