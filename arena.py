from character import Character
from random import randrange

# define class Arena
class Arena:
    # initialize class
    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B

    # methods
    def print_state(self):
        print("~"*15)
        # print team A
        print(("TEAM A").center("~"))
        for character in self.team_A:
            character.print()

        # print team B
        print(("TEAM B").center("~"))
        for character in self.team_B:
            character.print()

        print("~"*15)

    def play(self):
        time = -1   # unit to control time
        while True:
            time += 1 # increase after each round
            print("~"*15)
            print("Time = " + str(time))

            self.print_state()

            # create list of characters to play
            chars_to_play = []
            # eligible from team A
            for character in self.team_A:
                if character.delay == 0:
                    chars_to_play.append(('A',character))
            # eligible from team B
            for character in self.team_B:
                if character.delay == 0:
                    chars_to_play.append(('B',character))

            # active characters attack
            for character in chars_to_play:
                attacking = character[1]
                if character[0] == 'A':
                    defending = randrange(len(self.team_B))
                else: # character is in team B
                    defending = randrange(len(self.team_A))

                # attacking deals damage to defending thus decreases their health
                damage = attacking.attack()
                defending.health -= damage
                print(f"{attacking.character_name} dealt {damage} damage to {defending.character_name}")

            # check for dead characters in team A
            for pos in range(len(self.team_A)-1, -1, -1):
                if self.team_A[pos].is_dead():
                    print(f"{self.team_A[pos].character_name} is dead!")
                    self.team_A.pop(pos)
            # same for team B
            for pos in range(len(self.team_B)-1, -1, -1):
                if self.team_B[pos].is_dead():
                    print(f"{self.team_B[pos].character_name} is dead!")
                    self.team_B.pop(pos)
            
            # check if game ended
            if len(self.team_A) == 0:
                print("Team B won!")
                break
            elif len(self.team_B) == 0:
                print("Team A won!")   
                break

            # end round
            for character in self.team_A:
                character.end_round()
            
            for character in self.team_B:
                character.end_round()
            
            input("Press Enter to Continue")