# Basic Dictionary.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Indonesia": "Jakarta"
}

# Nested List in Dictionary.
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# Challenge.
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["AA", "AB"], "C", "D", ["CC", "CD"], ["AC", "AD", "BC", "BD", ["ABC", "BCD", ["ABCD", "BCDA"]]]]
# print(nested_list[2][0])
# print(nested_list[2][1])
#
# print(nested_list[6])
# print(nested_list[6][4])
# print(nested_list[6][4][2])
# print(nested_list[6][4][2][1])

# Dictionary inside of Dictionary.
travel_log = {
    "France": {
        "Cities_Visited": ["Paris", "Lille", "Dijon"],
        "Times_Visited": 12
    },
    "Germany": {
        "Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Times_Visited": 5
    }
}
print(travel_log)

# Challenge 2.
print(travel_log["Germany"]["Cities_Visited"][2])
