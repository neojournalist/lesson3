weatherCondition = 'There is a rain'
weatherCondition2 = 'There is no rain'

currentWeather = 'There is a rain'
#if else clause
if currentWeather == weatherCondition:
    print('Take an umbrella')
else:
    print('Do not take an umbrella')

#check the age between 25 and 40 including
age = int(input('Your age: '))

if age >= 25 and age <= 40:
    print('You are accepted!')
else:
    print('You are not accepted')

# if the age is 41 then TRUE BECAUSE TRUE OR false is TRUE
if age >= 25 or age <= 40:
    print('You are accepted!')
else:
    print('You are not accepted')

name1 = 'Aslan'
name2 = 'Sergei'
name3 = 'Timur'
name4 = 'Altynai'

nameToCheck = 'Aslan'
if nameToCheck == name1 or nameToCheck == name2 or nameToCheck == name3 \
    nameToCheck == name4:
    print('We need you!')

# if else, elif else if
address1 = 'Mira 1'
address2 = 'Turusbekova 7'

deliveryAddress = input('Delivery address:')

if deliveryAddress == address1:
    print('Get your delivery!')
elif deliveryAddress == address2:
    print('Get your delivery')
else:
    print('Your delivery has not arrived yet')

#Nested if else
age = int(input('Your age: '))

if age >= 18:
    print('You can vote')
    if age == 18:
        print('You are getting a present on your first vote!')
    elif age >= 100:
        print('You can vote from home')
    else:
        print('Ypu cannot get a present, it isnot your first vote!')
else:
    print('You cannot vote')