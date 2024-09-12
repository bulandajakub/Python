populations = {
    "United States": 331449281,
    "Nigeria": 206139589,
    "India": 1380004385,
    "Kenya": 54771231,
    "Philippines": 111046913,
    "Ghana": 31255435,
    "Brazil": 213947263,
    "South Africa": 59622350,
    "Pakistan": 220892340,
    "Canada": 38008005
}

'''
Write a program that asks the user to enter the name of a country
and then prints its population. If the user enters a country
that is not in the dictionary, the program should print a message
saying that it doesn't have information on that country.
'''

def country_populations():
    country = input("Enter the name of a country: ").title()
    population = populations.get(country)
    if population is None:
        print("We don't have information on that country.")
    else:
        print(population)


country_populations()
