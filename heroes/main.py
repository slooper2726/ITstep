heroes = []
things = []
hero_count = int(input("how many heroes do you have in your team? "))
index = 0
while index < hero_count:
    print('hero', index + 1)
    hero = input('please enter your name: ')
    thing = input('name 3 things you will take with yourself for campaign: ')
    heroes.append(hero)
    things.append(thing)
    index = index + 1
print('Campaign:')
index = 0
while index < hero_count:
    print('hero', index + 1)
    print('name: ', heroes[index])
    print('things: ', things[index])
    index = index + 1
