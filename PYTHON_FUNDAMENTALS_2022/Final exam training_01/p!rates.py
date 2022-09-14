def creation_of_cities_list(cities, comm):
    while comm[0] != "Sail":

        city = comm[0]
        gold = int(comm[2])
        citizens = int(comm[1])
        if city not in cities:
            cities[city] = [citizens, gold]
        else:
            cities[city][0] += citizens
            cities[city][1] += gold
        comm = input().split("||")
    return cities


def events_for_cities_list(cities):
    while True:
        command = input().split("=>")
        if command[0] == "End":
            break
        elif command[0] == "Plunder":
            town = command[1]
            people = int(command[2])
            stolen_gold = int(command[3])
            if town in cities:
                cities[town][1] -= stolen_gold
                cities[town][0] -= people
                print(f"{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")
                if cities[town][0] == 0 or cities[town][1] == 0:
                    del cities[town]
                    print(f"{town} has been wiped off the map!")
            else:
                continue

        elif command[0] == "Prosper":

            town = command[1]
            given_gold = int(command[2])

            if given_gold >= 0:
                cities[town][1] += given_gold
                print(f"{given_gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

            else:
                print(f"Gold added cannot be a negative number!")
                continue

    return cities


def additional_print(cities):
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    if cities:
        for town in cities:
            people = cities[town][0]
            gold = cities[town][1]

            print(f"{town} -> Population: {cities[town][0]} citizens, Gold: {cities[town][1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def main_cities_list(cities):
    cities = {}
    creation_of_cities_list(cities, comm)
    events_for_cities_list(cities)
    additional_print(cities)


comm = input().split("||")
main_cities_list(comm)
