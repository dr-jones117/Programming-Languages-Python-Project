# Grading tags in for all lines marked with *               ___
#
# Tierless str meets D in SOLID(hidden test)*		        _DONE_
# Check if above is done, but not its test was not reached	___
#
# 1. Initial Show system\Got it compiling
# Menu\initial system working					    _DONE_
# Bad input handled						            _DONE_
#
# 2. Add Default
# Added and shown properly					        _DONE_
# Secon d+ item ignored						        _DONE_
#
# 3. Basic Update (single)
# Moves along section						        _DONE_
# String format correct						        _DONE_
# Iterator use d*							        _DONE_
#
# 4. Basic Update (multiple)					    _DONE_
#
# 5. Multi Update
# Updates correctly						            _DONE_
# Bad input handled						            _DONE_
#
# 6. Show details
# Shows details properly 						    _DONE_
# Iterator use d*							        _DONE_
#
# 6. Add user specified item
# Basic movement still works					    ___
# Powered works							            ___
# No passing							            ___
#
# 7. Tester part 1
# Boats works up to second lock 					___
# Formatting correct 						        ___
#
# 8. Tester part 2
# Boats works up to end						        ___
# Strategy pattern for basic fil l*				    ___
#     Strategy pattern for fast empt y*				___
#
# 9. Custom belt **
# String formatting correct					        ___
# Everything still works 						    ___
# Bad input handled 						        ___
from MorganJonah.BoatBehavior.BoatBehavior import SteadyBoatBehavior, MaxSpeedBoatBehavior
from MorganJonah.RiverPart.Lock import Lock
from MorganJonah.RiverPart.Section import Section
from RiverSystem import RiverSystem
from RiverPart.Boat import Boat

boat_id = 1


def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()

    return result


def main():
    menu = "\n" \
           "1) Add Default Boat\n" \
           "2) Update One Tick\n" \
           "3) Update X Ticks\n" \
           "4) Show Section Details\n" \
           "5) Add Boat\n" \
           "6) Make Tester\n" \
           "7) Make New Simulator\n" \
           "0) Quit\n"

    global boat_id
    river_system = RiverSystem()
    print(river_system)

    choice = -1
    while choice != 0:
        try:
            print(menu)
            choice = int(cleanInput("Choice:> "))

            # add default box
            if choice == 1:
                add_default_boat(boat_id, river_system)
                boat_id += 1

            # update one time
            elif choice == 2:
                river_system.update()
                print(river_system)

            # update X number of times
            elif choice == 3:
                run_multiple_updates(river_system)

            # print out station details
            elif choice == 4:
                show_section_details(river_system)

            # make a new box of any size
            elif choice == 5:
                add_boat(boat_id, river_system)
                boat_id += 1

            # make new system
            elif choice == 6:
                river_system.make_tester_river()
                print(river_system)

            # make new system
            elif choice == 7:
                print("TODO")

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                hidden_command(river_system)

            elif choice == 0:
                choice = 0

            elif choice < -1 or choice > 7:
                print("Input an option in the range 0-7")
        except ValueError:
            # import traceback
            # print(traceback.format_exc())
            print('Please, input a positive integer')


def add_boat(boat_id: int, river_system: RiverSystem):
    power = int(cleanInput("What engine power:> "))
    travel_method = int(cleanInput("What travel method. (1) Steady or (2) Max :> "))
    if travel_method < 1 or travel_method > 2:
        print('Input an option in the range 1-2')
        print(river_system)
        return

    boat = None
    if travel_method == 1:
        boat = Boat(boat_id, power, SteadyBoatBehavior())
    elif travel_method == 2:
        boat = Boat(boat_id, power, MaxSpeedBoatBehavior())

    river_system.add_boat(boat)
    print(river_system)



def add_default_boat(boat_id: int, river_system: RiverSystem):
    new_boat = Boat(boat_id)
    river_system.add_boat(new_boat)
    print(river_system)



def hidden_command(river_system: RiverSystem):
    test_section = Section()
    test_lock = Lock()

    boat_one = Boat(1)
    boat_two = Boat(2)
    boat_three = Boat(3)

    test_section.receive_boat(boat_one)
    test_lock.receive_boat(boat_two)
    river_system.add_boat(boat_three)

    # GRADING: TO_STR
    print(boat_one)
    print(test_section)
    print(test_lock)
    print(river_system)


def run_multiple_updates(river_system: RiverSystem):
    choice = int(cleanInput("How many updates:> "))
    for _ in range(choice):
        river_system.update()
        print(river_system)


def show_section_details(river_system: RiverSystem):
    river_system.show_section_details()


if __name__ == '__main__':
    main()
