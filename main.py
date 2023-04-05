# import Character and Arena classes
from character import Character
from arena import Arena
# include randomization tool
from random import randrange

# define main
def main():
    # team A consisted of 5 Orcs
    orcs = [Character("Orc-" + str(i+1), 2, randrange(4)) for i in range(5)]
    # team B consisted of 3 Night Elves
    night_elves = [Character("Night-Elf-" + str(i+1), 3, randrange(3)) for i in range(3)]

    a = Arena(orcs, night_elves)
    a.play()


# call main
main()
