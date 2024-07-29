# Dictionary

# Naming the dictionary
dayconverter = {
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday"
}

# Use unique keys

print(dayconverter)
# Output: {'Sun': 'Sunday', 'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thu': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday'}

print(dayconverter["Thu"])
# Output: Thursday

"""
print(dayconverter["Moy"])
there is no such key in the dictionary, so here we get a 
KeyError: 'Moy'
"""

print(dayconverter.get("Fri"))
# Output: Friday

print(dayconverter.get("Fii"))
# Output: None

print(dayconverter.get("hay", "This is an invalid key"))
# Output: This is an invalid key
