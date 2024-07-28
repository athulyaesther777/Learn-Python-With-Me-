# List in Python

countries = ["Germany", "Brazil", "Ireland", "Canada"]
print(countries)  # Output: ['Germany', 'Brazil', 'Ireland', 'Canada']

# now lets look how index values works (start with 0)
print(countries[0])  # Output: Germany
print(countries[3])  # Output: Canada
print(countries[-2])  # Output: Ireland

# false is a boolean value so that there is no need of any "
mix = ["Germany", 1940, False]
print(mix)  # Output: ['Germany', 1940, False]

print(countries[2:])  # Output: ['Ireland', 'Canada']
# look it carefully, here we took 2 to end

print(countries[0:2])  # Output: ['Germany', 'Brazil']
# here we didn't take the last 2 ones, it only prints 0 and 1 index values

print(countries[-1:])  # Output: ['Canada']
# the -1 shows the last one

print(countries[:-1])  # Output: ['Germany', 'Brazil', 'Ireland']
# now look what happened, it avoids the last one and prints the rest

print(countries[:])  # Output: ['Germany', 'Brazil', 'Ireland', 'Canada']
# now we can see that it prints the whole list when we give ':'

print(countries[:2])  # Output: ['Germany', 'Brazil']
# now it prints the 0 and 1 index values

countries[1] = "London"
print(countries)  # Output: ['Germany', 'London', 'Ireland', 'Canada']
# now look we replaced Brazil with London
