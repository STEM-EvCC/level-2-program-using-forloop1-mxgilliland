mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# create a variable to store the total number of missions
mission_total = int(len(mission_names))

#        Counts the number of successful missions.

# create a variable to store the number of successful missions, aka all of the missions labeled as True
true_counter = True

mission_success_total = mission_success.count(true_counter)

#        Calculates the success rate of the missions.

# create a variable to store the total of the success rate, which will also be an equation
success_rate = (mission_success_total / mission_total) * 100
shorter_success_rate = round(success_rate, 2)

#        Lists all the missions that were launched before the year 2000.

# this should be a length check, for the mission years maybe? excluding the mission in 2012
missions_pre_2000 = len(mission_years)

#        Count the total number of missions.
#        Count the number of successful missions.
#        Identify and list all missions launched before the year 2000.

#    Output the Results:
#        Print the total number of missions.

# this will most likely be a print statement to print out the total from the variable
print("Total number of missions: " + str(mission_total))

#        Print the number of successful missions.

# this will likely be another print statement with the success variable
print("Number of successful missions: " + str(mission_success_total))

#        Print the success rate as a percentage.

# will likely be a float
print("Success rate: " + str(shorter_success_rate) + "%")

#        Print the names of the missions launched before the year 2000.

print("Missions launched before the year 2000: ")

#        Use a for loop to iterate through the list of missions.
for i in range(len(mission_names)):
    if mission_years[i] < 2000:
        print(f"- {mission_names[i]}")