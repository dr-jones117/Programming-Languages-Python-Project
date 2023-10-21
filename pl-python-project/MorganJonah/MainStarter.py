from RiverCode.RiverSystem import RiverSystem
from RiverCode.Boat import Boat

boat_id = 1
river_system = RiverSystem()

def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()

    return result


def update():
    return

def add_default_boat():
    river_system.add_boat(Boat(boat_id))

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

    print(river_system)

    choice = -1
    while choice != 0:
        print(river_system)
        print(menu)
        choice = cleanInput("Choice:> ")
        try:
            choice = int(choice)
            if choice == 1:
                add_default_boat()

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

            elif choice < 0 or choice > 7:
                choice = 0
            else:
                print("Input an option in the range 0-7")

        except ValueError:
            import traceback
            print(traceback.format_exc())
            print('Please, input a positive integer.')


if __name__ == '__main__':
    main()

