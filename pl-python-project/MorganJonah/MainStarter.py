# Grading tags in for all lines marked with * ___
#
# Tierless str meets D in SOLID(hidden test)*		___
# Check if above is done, but not its test was not reached	___
#
# 1. Initial Show system\Got it compiling
# Menu\initial system working					    ___
# Bad input handled						            ___
#
# 2. Add Default
# Added and shown properly					        ___
# Secon d+ item ignored						        ___
#
# 3. Basic Update (single)
# Moves along section						        ___
# String format correct						        ___
# Iterator use d*							        ___
#
# 4. Basic Update (multiple)					    ___
#
# 5. Multi Update
# Updates correctly						            ___
# Bad input handled						            ___
#
# 6. Show details
# Shows details properly 						    ___
# Iterator use d*							        ___
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

from RiverSystem import RiverSystem
from RiverPart.Boat import Boat


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

    boat_id = 1
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
                print("TODO")

            # update X number of times
            elif choice == 3:
                print("TODO")

            # print out station details
            elif choice == 4:
                print("TODO")

            # make a new box of any size
            elif choice == 5:
                print("TODO")

            # make new system
            elif choice == 6:
                print("TODO")

            # make new system
            elif choice == 7:
                print("TODO")

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                print("TODO")

            elif choice == 0:
                choice = 0

            elif choice < -1 or choice > 7:
                print("Input an option in the range 0-7")
        except ValueError:
            # import traceback
            # print(traceback.format_exc())
            print('Please, input a positive integer')


def add_default_boat(boat_id: int, river_system: RiverSystem):
    new_boat = Boat(boat_id)
    river_system.add_boat(new_boat)
    print(river_system)


if __name__ == '__main__':
    main()
