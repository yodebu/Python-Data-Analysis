#!/usr/bin/env python
 
# MontyHall.py
 
# Library used - Numpy for its numpy.random() modules 
# The Monty Hall problem: 
# You are on a gameshow and are
# presented with three doors. Behind one door (chosen at rand) sits a prize.
# You must select (guess) a door. If you guess correctly, you get the prize.
# But, when you select your door, the show's host throws in a bit of a twist,
# opening one of the other two doors ... specifically a door that doesn't
# contain the prize. He asks you if you'd like to change your door selection,
# to the only other remaining door (not the one you picked originally and not
# the now open door). Do you change your selection? Why?
 
# Answer: Yes. ALWAYS change your selection. By sticking with your original
# door selection, you have a 1/3 chance of getting the prize. By switching, you
# end up with a 2/3 chance of getting the prize.
 
 

import numpy as np 

# We need the Numpy module to use its random function value
#  which provides a Return random integers from low (inclusive) to high (exclusive).
 
 
def pick_door():
    """
    Function to pick a door. Returns an integer 1, 2, or 3 at random.
    """
    return np.random.randint(1,4) 
 
 
class MontyHall:
    """
    Class to model the Monty Hall problem.
    """
    def __init__(self):
        """
        Class Constructor -initializes values to the program
        Creates an instance of the Monty-Hall problem. This will be called
        automatically when the class is formed.
        """
        
        # Pick a prize door randomly and store as a variable.
        
        self.prize_door = pick_door()
        
        # We'll create variables for the selected door and removed door as
        # well, but we won't set them just yet.
        
        self.selected_door = None
        self.removed_door = None
 
 
    def select_door(self):
        """
        randomly selects a door for the contestant.
        """
        self.selected_door = pick_door()

 
    def remove_door(self):
        """
        This is how the host removes a (non-prize/non-selected) door
        """
        # Pick a door at random.
        d = pick_door()
        # If that door is the prize door or the contestant's door, re-pick.
        while d == self.selected_door or d == self.prize_door:
            d = pick_door()
        # set the removed door to d
        self.removed_door = d
 
    
    
    def switch_choice(self):
        """
        Switches the selected door once a non-prize door is removed.
        """
        # 1+2+3=6. There's only one choice of door if we switch our selection.
        self.selected_door = 6 - self.selected_door - self.removed_door
 
    
    
    def user_wins(self):
        """
        Determine if the user wins. Return true on win, false on lose.
        """
        if self.selected_door == self.prize_door:
            return True
        else:
            return False
 
    
    
    def run_game(self, switch=True):
        """
        Once a problem is initialized, run the game.
 
        'switch' determines if the user changes selection during the game.
        """
        # The user selects a door.
        self.select_door()
        # The host removes a door.
        self.remove_door()
        # The user can switch selection of doors.
        if switch:
            self.switch_choice()
        # Determine if the user wins.
        return self.user_wins()
 
 
def main():
    # Now, we'll run the game. When asked if we want to switch door selection when
    # the door is removed by the host, we'll say 'yes' and switch our choice of
    # door. We'll run that experiment one million times, always switching choice
    # when given the chance. Here's what that looks like:
 
    wins, losses = 0, 0
    
    for i in range(1000000):
        # make an instance of the game, call it 'm'
        m = MontyHall()
        # run the game and switch choice of door.
        if m.run_game(switch=True):
            # a return value of True means we've won
            wins += 1
        else:
            # a return value of False means we've lost
            losses += 1
 
    # Now that the game has been run one million times, compute/display stats.
    perc_win = 100.0*wins / (wins+losses)
 
    print "\nOne million Monty Hall games (with switching):"
    print "  won:", wins, "games"
    print "  lost:", losses, "games"
    print "  odds: %.2f%% winning percentage" % perc_win
 
 
    # Now, we'll run the game one million times and always stick to our original
    # door selection every single time.
 
    wins, losses = 0, 0
    for i in range(1000000):
        # make an instance of the game, call it 'm'
        m = MontyHall()
        # run the game and switch choice of door.
        if m.run_game(switch=False):
            # a return value of True means we've won
            wins += 1
        else:
            # a return value of False means we've lost
            losses += 1
 
    # Now that the game has been run one million times, compute/display stats.

    perc_win = 100.0*wins / (wins+losses)
 
    print "\nOne million Monty Hall games (staying with original choice):"
    print "  won:", wins, "games"
    print "  lost:", losses, "games"
    print "  odds: %.2f%% winning percentage\n" % perc_win




if __name__ == '__main__':
    main()