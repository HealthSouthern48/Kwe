# =================================================================
# file:         defaults.rpy
# description:  Default values for the game
# author:       Sheikh Saad Abdullah (A00447871)
# =================================================================

# common defaults
default player_name = "Player"
default flag = False

# default values for chapter 1
default passed_say = ""
default nothing = False
default last_say = "Anything else on your list?"
default stock = {"milk": 1.25, "tomatoes": 2.50, "eggs": 1.50, "potatoes": 4.75}
default cart = {"milk": False, "tomatoes": False, "eggs": False, "potatoes": False}

init python:
    def out_of_stock():
        if all(cart.values()):
            s("Sorry, we're out of stock.")
            extend(" Please come by later for more fresh groceries.")
            renpy.jump("checkout")

# TODO: default values for chapter 2

# TODO: default values for chapter 3
