# Grading tags in for all lines marked with *                _DONE_
#
# Tierless str meets D in SOLID(hidden test)*		         _DONE_
# Check if above is done, but not its test was not reached	 _Test was reached!_
#
# 1. Initial Show system\Got it compiling
# Menu\initial system working					    _DONE_
# Bad input handled						            _DONE_
#
# 2. Add Default
# Added and shown properly					        _DONE_
# Second+ item ignored						        _DONE_
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
# Basic movement still works					    _DONE_
# Powered works							            _DONE_
# No passing							            _DONE_
#
# 7. Tester part 1
# Boats works up to second lock 					_DONE_
# Formatting correct 						        _DONE_
#
# 8. Tester part 2
# Boats works up to end						        _DONE_
# Strategy pattern for basic fil l*				    _DONE_
#     Strategy pattern for fast empty*				_DONE_
#
# 9. Custom belt **
# String formatting correct					        _DONE_
# Everything still works 						    _DONE_
# Bad input handled 						        _DONE_

"""
River Simulation System

This script implements a river simulation system that allows users to interact with a river
system. The available functionality is explained below.

The script provides the following functionality:
1. Add a default boat to the river.
2. Update the simulation for a single time step.
3. Update the simulation for 'n' number of time steps.
4. Show the details of each section in the river.
5. Add boats to the river with specified power and behaviors.
6. Create a tester river with predefined components for debugging.
7. Create a new river system with custom sections and locks.

Author: Jonah Morgan
Date: 10/21/2023
"""

from morgan_jonah.BoatBehavior.MaxSpeedBoatBehavior import MaxSpeedBoatBehavior
from morgan_jonah.BoatBehavior.SteadyBoatBehavior import SteadyBoatBehavior
from morgan_jonah.LockBehavior.BasicLockBehavior import BasicLockBehavior
from morgan_jonah.LockBehavior.FastLockBehavior import FastLockBehavior
from morgan_jonah.LockBehavior.PassThroughLockBehavior import PassThroughLockBehavior
from morgan_jonah.RiverSystem.RiverParts.Lock import Lock
from morgan_jonah.RiverSystem.RiverParts.Section import Section
from morgan_jonah.RiverSystem.RiverSystem import RiverSystem
from morgan_jonah.RiverSystem.RiverParts.Boat import Boat

boat_id = 1


def cleanInput(prompt):
    """
    Get user input and ensure it is not empty.

    This function prompts the user with the given message (prompt) and
    ensures that the input is not empty. If the user provides an empty
    input.

    Args:
        prompt (str): The message to display when requesting input.

    Returns:
        str: The non-empty user input.

    Example:
        result = cleanInput("Enter your name: ")
    """
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()

    return result


def main():
    """
    Main function for the River Simulation System.

    This function serves as the entry point for the river simulation system.
    It provides a menu for users to interact with the simulation, including
    options to add boats, update the simulation, and customize the river system.

    Args:
        None

    Returns:
        None
    """
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

            # add default boat
            if choice == 1:
                add_default_boat(river_system)
                boat_id += 1

            # update one tick
            elif choice == 2:
                river_system.update()
                print(river_system)

            # update X number of ticks
            elif choice == 3:
                run_multiple_updates(river_system)

            # print out station details
            elif choice == 4:
                show_section_details(river_system)

            # make a new box of any size
            elif choice == 5:
                add_boat(river_system)
                boat_id += 1

            # make new system
            elif choice == 6:
                river_system.make_tester_river()
                print(river_system)

            # make new system
            elif choice == 7:
                make_river_command(river_system)

            # debug/check for D in SOLID in __str__
            elif choice == -1:
                hidden_command(river_system)

            # exit the program
            elif choice == 0:
                choice = 0

            elif choice < -1 or choice > 7:
                print("Input an option in the range 0-7")

        except ValueError:
            # import traceback
            # print(traceback.format_exc())
            print('Please, input a positive integer')


def add_boat(river_system: RiverSystem):
    """
    Add a boat to the river system with customizable attributes.

    This function allows the user to add a boat to the river system
    with customizable power and travel methods. The user is prompted
    for input regarding the boat's characteristics, and then the
    boat is added to the river system.

    Args:
        river_system (RiverSystem): The river system to which the boat is added to.

    Returns:
        None

    Example:
        add_boat(river_system)
    """
    global boat_id
    power = int(cleanInput("What engine power:> "))
    travel_method = int(cleanInput("What travel method. (1) Steady or (2) Max :> "))
    if travel_method < 1 or travel_method > 2:
        print('Input an option in the range 1-2')
        boat_id -= 1
        print(river_system)
        return

    boat = None
    if travel_method == 1:
        behavior = SteadyBoatBehavior()
        boat = Boat(boat_id, power, behavior)
    elif travel_method == 2:
        behavior = MaxSpeedBoatBehavior()
        boat = Boat(boat_id, power, behavior)

    river_system.add_boat(boat)
    print(river_system)


def add_default_boat(river_system: RiverSystem):
    """
    Add a default boat to the river system.

    This function adds a default boat to the river system.
    The default boat is added without specifying custom power
     or travel methods.

    Args:
        river_system (RiverSystem): The river system the boat
        will be added to.

    Returns:
        None

    Example:
        add_default_boat(river_system)
    """
    global boat_id

    new_boat = Boat(boat_id)
    river_system.add_boat(new_boat)
    print(river_system)


def hidden_command(river_system: RiverSystem):
    """
    Run the hidden command for D in SOLID print testing.

    This function is used for debugging and allows the user to perform THE
    hidden command. It creates a test section, test lock, and three test boats.
    Afterward, it prints these objects. Which adheres to the D in SOLID.

    Args:
        river_system (RiverSystem): The river system to which
        objects are added and printed.

    Returns:
        None

    Example:
        hidden_command(my_river_system)
    """
    global boat_id

    test_section = Section()
    test_lock = Lock()

    boat_one = Boat(boat_id)
    boat_id += 1
    boat_two = Boat(boat_id)
    boat_id += 1
    boat_three = Boat(boat_id)
    boat_id += 1

    test_section.receive_boat(boat_one)
    test_lock.receive_boat(boat_two)
    river_system.add_boat(boat_three)

    # GRADING: TO_STR
    print(boat_one)
    print(test_section)
    print(test_lock)
    print(river_system)


def run_multiple_updates(river_system: RiverSystem):
    """
    Update the river system for multiple ticks.

    This function allows the user to update the river system
    for a specified number of time steps. It prompts the user
    for the number of updates and then iteratively updates the
    river system. The updated river system is printed after
    each update.

    Args:
        river_system (RiverSystem): The river system to be updated.

    Returns:
        None

    Example:
        run_multiple_updates(my_river_system)
    """
    choice = int(cleanInput("How many updates:> "))
    for _ in range(choice):
        river_system.update()
        print(river_system)


def show_section_details(river_system: RiverSystem):
    """
    Show details of each section in the river system.

    This function displays details of each section in the
    river system, such as section ID, amount of boats, and flow.

    Args:
        river_system (RiverSystem): The river system for which
        section details are displayed.

    Returns:
        None

    Example:
        show_section_details(my_river_system)
    """
    river_system.show_section_details()


def make_river_command(river_system: RiverSystem):
    """
    Create a new river system with custom sections and locks.

    This function allows the user to create a new river system
    by adding custom sections and locks.
    Args:
        river_system (RiverSystem): The river system to
        which custom components are added.

    Returns:
        None

    Example:
        make_river_command(my_river_system)
    """
    river_system.clear()
    keep_adding_parts = True
    section_id = 1

    while keep_adding_parts:
        try:
            choice = int(cleanInput("Section (1) or Lock (2):> "))
            if choice < 1 or choice > 2:
                print('Input an option in the range 1-2')
            elif choice == 1:
                length = int(cleanInput("Length:> "))
                flow = int(cleanInput("Flow:> "))
                river_system.add_river_part(Section(length, flow, section_id))
                section_id += 1

            elif choice == 2:
                behavior = int(cleanInput("Fill behavior: None (1), Basic (2), or Fast Empty (3):> "))
                depth = int(cleanInput("Depth:> "))

                if behavior == 1:
                    behavior = PassThroughLockBehavior()
                elif behavior == 2:
                    behavior = BasicLockBehavior()
                elif behavior == 3:
                    behavior = FastLockBehavior()

                river_system.add_river_part(Lock(depth, behavior))

        except ValueError:
            print('Cannot accept value')

        continue_adding = cleanInput("Add another component (n to stop):> ")
        if continue_adding == 'n':
            keep_adding_parts = False

    print(river_system)


if __name__ == '__main__':
    main()
