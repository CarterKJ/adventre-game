import time
import random
winInt = 250
bal = 0
hunger = 23
food = 0
repair = 0
miles = 0
pace = ''
foodln = ''
days = 0
ldays = 20

def classChoice():
    global bal
    print("""
Enter the class you want to be:
Banker, $1000
Black Smith, $500
Farmer, $200
""")
    time.sleep(1)

    while True:
        classID= input('>').lower()

        if 'banker' in classID:

            bal += 1000
            print('You have chosen Banker')
            startShop()
            break
        elif 'black smith' in classID:
            bal +=500
            print('You have chosen Black Smith')
            startShop()
            break
        elif 'farmer' in classID:
            bal += 200
            print('You have chosen Farmer')
            startShop()
            break
        else:
            print('hmmm seems thats not a thing yet, try again')






def startMenu():
    global bal
    global food
    global winInt
    global hunger
    global ldays
    print('Enter name to be saved as')
    name = input('>')
    time.sleep(1)
    print(f"Hi {name} to get started type 'start'")
    time.sleep(1)
    startScreen = input('>').lower
    eldless = input('endless mode? y/n:')
    if 'y' in eldless:
        winInt = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
        ldays = 999999999999999999999999999999999999999999999999999999999999999999999999999999999


    if 'start' in startScreen():
        classChoice()

    elif '00100100' in startScreen():
        bal = 1000000
        food = 100000000
        hunger = 1000000
        classChoice()


def startShop():
    global bal
    global food
    global repair

    print("""
    
    """)
    print('Welcome to the shop')
    time.sleep(1)
    print('Here you can buy everything you need.')
    time.sleep(.5)
    print("""
Food $7
Parts $10
    """)
    time.sleep(.5)
    print(f'you have ${bal}')
    time.sleep(1)
    print('to buy something type what you want to buy the wait, type how much you want')
    print("'cart' to see what you have")
    print("And 'ready' when you are ready to leave")
    time.sleep(1)

    while True:
        startCart = input('>').lower()
        if 'food' in startCart:
            start_max_food = bal / 7

            startFoodAmount = int(input('How much of that would you like:'))

            if startFoodAmount > start_max_food:
                print('you dont have enough')
            else:
                bal = bal - (startFoodAmount*7)
                food = food + startFoodAmount
                print(f'you have ${bal}')

        elif  'parts' in startCart:
            start_max_parts = bal / 10

            startPartAmount = int(input('How much of that would you like:'))

            if startPartAmount > start_max_parts:
                print('you dont have enough')
            else:
                bal = bal - (startPartAmount*7)
                repair = repair + startPartAmount
                print(f'you have ${bal}')
        elif 'cart' in startCart:
            print('You have:')
            time.sleep(.8)
            print(f'{food} lbs of food')
            print(f'{repair} parts')
            print(f'${bal}')
        elif 'ready' in startCart:
            start()
        else:
            print('I dont sell that here')



def start():
    print("""
    
    """)
    print('You are about to start your journey')
    time.sleep(.4)
    print('do you have everything you need? y/n')
    time.sleep(.4)
    reprat_shop = input('>').lower()
    if 'n' in reprat_shop:
        startShop()
    time.sleep(1)
    print('You have started your journey')
    print("You can eat and rest by typing 'menu' on rest ocactions")
    time.sleep(1)
    print('before you start enter these settings')
    menu()

def menu():
    global bal
    global food
    global repair
    global miles
    global foodln
    global pace
    global hunger
    global days
    time.sleep(.1)
    print("enter pace, 'fast', normal, slow")
    PaceInput = input('>').lower()
    if 'fast' in PaceInput:
        pace = 30
    elif 'normal' in PaceInput:
        pace = 17
    elif 'slow' in PaceInput:
        pace = 8
    time.sleep(1)
    print("Enter food servings,'lots', 'normal','barebones'")
    foodInput = input('>').lower()
    if 'lots' in foodInput:
        foodln = 'lots'
    elif 'normal' in foodInput:
        foodln = 'normal'
    elif 'barebones' in foodInput:
        foodln = 'low'
    day1()

def day1():
    global bal
    global food
    global repair
    global miles
    global foodln
    global pace
    global hunger
    global days
    days +=1

    if pace == 30:
        hunger = hunger - 15
        miles += 20
    elif pace == 17:
        hunger = hunger -9
        miles += 17
    elif  pace == 8:
        miles += 16
        hunger = hunger - 4

    if food > 0:
        if foodln == 'lots':
            food = food-4
            hunger = hunger + 19
        elif foodln == 'normal':
            food = food - 2
            hunger = hunger + 11
        elif foodln == 'low':
            food = food - 1
            hunger = hunger + 5
    if hunger <= 0:
        death()
    if hunger < 25:
        pace = 8

    print('This is your 1st day')
    time.sleep(.5)
    print(f'you have {hunger} hunger, if this hits 0 you will die')
    print(f'you have {food} lbs of food, make sure this is over 0')
    time.sleep(1)
    print(f'your day ends you have travled {miles} miles you start to doze off')
    print("""
    
    """)
    dayLoop()


def dayLoop():
    global ldays
    global bal
    global food
    global repair
    global miles
    global foodln
    global pace
    global hunger
    global days
    global winInt
    while True:
        days += 1
        if pace == 30:
            hunger = hunger - 15
            miles += 20
        elif pace == 17:
            hunger = hunger - 9
            miles += 17
        elif pace == 8:
            miles += 16
            hunger = hunger - 4

        if food > 0:
            if foodln == 'lots':
                food = food - 4
                hunger = hunger + 19
            elif foodln == 'normal':
                food = food - 2
                hunger = hunger + 11
            elif foodln == 'low':
                food = food - 1
                hunger = hunger + 5
        if hunger <= 0:
            death()
        if hunger < 25:
            pace = 8

        print(f'This is your {days} day')
        time.sleep(1.5)
        print(f'you have {hunger} hunger')
        time.sleep(1)
        print(f'you have {food} lbs of food')
        time.sleep(1)
        fate = random.randint(1, 100)
        if fate > 80:
            rng = 'sick'
        elif fate < 30:
                rng = 'broken down'
        else:
            rng = 'normal'

        if rng == 'broken down':
            print('your cant broke down')
            repair = repair - 2
            if repair < 0:
                broken()
        if rng == 'sick':
            print('Oh no, you got sick')
            time.sleep(1)
            print('you will have to rest 4 days')
            days += 4
            hunger = hunger - 13
            if hunger <= 0:
                death()

        if days % 7 == 0:
            print('you got into town')
            print('would you like to shop? y/n')
            town = input('>')
            if 'y' in town:
                Shop()

        menu_gate = input('would you like to enter the menu y/n:')
        if 'y' in menu_gate:
            mainMenu()
        print(f'your day ends you have travled {miles} miles you start to doze off')
        time.sleep(3)
        print("""
        
        
        """)
        if miles >= winInt:
            win()
        if days >= ldays:
            OutOfTime()

def death():
    global days
    print('you have died')
    time.sleep(1)
    print(f'you lasted {days} days')
    restart = input('Restart? y/n:')
    if 'y' in restart:
        startMenu()
    elif 'n'in restart:
        startMenu()

def broken():
    global days
    print('your cart broke down and you cant fix it')
    print('welp now what')
    print(f'you lasted {days} days')
    time.sleep(1)
    restart = input('Restart? y/n:')
    if 'y' in restart:
        startMenu()
    elif 'n'in restart:
        startMenu()


def Shop():
    global bal
    global food
    global repair
    global miles
    global foodln
    global pace
    global hunger
    global days

    print("""

    """)
    print('Welcome to the shop')
    time.sleep(1)
    print('Here you can buy everything you need.')
    time.sleep(.5)
    print("""
Food $7
Parts $10
    """)
    time.sleep(.5)
    print(f'you have ${bal}')
    time.sleep(1)
    print('to buy something type what you want to buy the wait, type how much you want')
    print("'cart' to see what you have")
    print("And 'ready' when you are ready to leave")
    time.sleep(1)

    while True:
        startCart = input('>').lower()
        if 'food' in startCart:
            start_max_food = bal / 7

            startFoodAmount = int(input('How much of that would you like:'))

            if startFoodAmount > start_max_food:
                print('you dont have enough')
            else:
                bal = bal - (startFoodAmount * 7)
                food = food + startFoodAmount
                print(f'you have ${bal}')

        elif 'parts' in startCart:
            start_max_parts = bal / 10

            startPartAmount = int(input('How much of that would you like:'))

            if startPartAmount > start_max_parts:
                print('you dont have enough')
            else:
                bal = bal - (startPartAmount * 7)
                repair = repair + startPartAmount
                print(f'you have ${bal}')
        elif 'cart' in startCart:
            print('You have:')
            time.sleep(.8)
            print(f'{food} lbs of food')
            print(f'{repair} parts')
            print(f'${bal}')
        elif 'ready' in startCart:
            dayLoop()
        else:
            print('I dont sell that here')

def mainMenu():
    global bal
    global food
    global repair
    global miles
    global foodln
    global pace
    global hunger
    global days
    time.sleep(.1)
    print("enter pace, 'fast', normal, slow")
    PaceInput = input('>').lower()
    if 'fast' in PaceInput:
        pace = 30
    elif 'normal' in PaceInput:
        pace = 17
    elif 'slow' in PaceInput:
        pace = 8
    time.sleep(1)
    print("Enter food servings,'lots', 'normal','barebones'")
    foodInput = input('>').lower()
    if 'lots' in foodInput:
        foodln = 'lots'
    elif 'normal' in foodInput:
        foodln = 'normal'
    elif 'barebones' in foodInput:
        foodln = 'low'
    dayLoop()


def win():
    print('Contrats you won!')
    print(f'you have ${bal} left')
    print(f'and {hunger} hunger left')
    time.sleep(1)
    restart = input('Restart? y/n:')
    if 'y' in restart:
        startMenu()

def OutOfTime():
    print('winter strikes')
    time.sleep(1)
    print('you did not make it')
    time.sleep(1)
    restart = input('Restart? y/n:')
    if 'y' in restart:
        startMenu()
    elif 'n'in restart:
        startMenu()



startMenu()
