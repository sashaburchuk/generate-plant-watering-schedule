#Plant Watering Schedule Program - Tells My significant Other How Often to Water Plants While I'm Away

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#plants[0] needs to be watered every 21 days
#plants[1,14] need to be watered every 7 days
#plants[15,20] need to be watered every 3 days

plants = ['Xanadu','Kangaroo Paw','Lemon Tree','Aloes','Cut Leaf Philodendron','Orchid','Fire Sticks','Cardamom Plants','Rock Orchid','Mist Fern','Fiddle Leaf Fig','Palms','Flowering Quince','Portulaca','Spider Plants','Chalk Sticks','Tree Fern','Bottlebrush','Nasturtiums','Aeolius','Any plants that are bone dry']


def dayNumber(dayToday):
    if dayToday == 'Monday':
        return 0
    if dayToday == 'Tuesday':
        return 1
    if dayToday == 'Wednesday':
        return 2
    if dayToday == 'Thursday':
        return 3
    if dayToday == 'Friday':
        return 4
    if dayToday == 'Saturday':
        return 5
    if dayToday == 'Sunday':
        return 6

weeksSince = int(input("How many weeks has it been since the Xanadu was last watered?"))

daysSince = int(input("How many days has it been since the Xanadu was last watered?"))



count = 3
confirm = input("I think today is " + days [(3 + daysSince) % 7] + " is that correct?")
while confirm != "yes":
    weeksSince = int(input("How many weeks has it been since the Xanadu was last watered?"))
    daysSince = int(input("How many days has it been since the Xanadu was last watered?"))
    confirm = input("You said " + str(daysSince) + ". Is that right?")
    if confirm != "yes":
        dayToday == int(input("What day of the week is today?"))
            


def showTodaysPlants(weeks, days):
    realDaysSince = weeks * 7 + days
    if realDaysSince % 21 == 0:
        print("\tWater Xanadu")
    if realDaysSince % 7 == 0:
        for plant in plants[1:14]:
            print("\tWater", plant)
    if realDaysSince % 3 == 0:
        for plant in plants[15:20]:
            print("\tWater", plant)


count = 0
vacationLength = int(input("How many days will Sasha be gone?"))
while count < vacationLength:
        print(days[(daysSince+count) % 7])
        showTodaysPlants(weeksSince, daysSince + count)
        print('\n')
        count = count + 1


