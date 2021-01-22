import random
import time 

# lists with numbers for game
nubmbers_for_players = [i for i in range(1,100)]
game_numbers = [i for i in range(1,100)]

# generates unique playing card for player
def create_play_card():
    player_card = []
    for i in range(0,5):
        n = random.choice(nubmbers_for_players)
        nubmbers_for_players.remove(n)
        player_card.append(n)
    return player_card

class Player:
    def __init__(self, name):
        self.name = name
        # creates game cards for players
        self.player_card = create_play_card()

    def specify_host(self, host_is):
        self.host = host_is
    
    def new_number(self, new_number):
        if new_number in self.player_card:
            if len(self.player_card) == 1:
                self.player_card.remove(new_number)
                self.host.winner_is(self.name)
            else:
                self.player_card.remove(new_number)
                self.host.found_number(self.name, new_number)
    
class GameHost:
    def __init__(self):
        self.numbers = set()
        self.players = set()
    
    def add_player(self, player):
        self.players.add(player)
        player.specify_host(self)
    
    def display_players(self):
        for player in self.players:
            print(player.name)
            print(player.player_card)
    
    def add_num(self, num):
        self.numbers.add(num)
        self.got_number(num)
    
    def got_number(self, new_number):
        print('We got number: %s' % (new_number))
        for player in self.players:
            player.new_number(new_number)

    def found_number(self, name, num):
        print('%s found number - %s' % (name, num))

    def winner_is(self, who):
        print('%s BINGO!!!' % (who.upper()))
        global winner
        winner = True

# game host
ghost = GameHost()

# initiating players
alex = Player('Alex')
john = Player('John')
anna = Player('Anna')
lisa = Player('Lisa')
karl = Player('Karl')

# adding players to game
ghost.add_player(alex)
ghost.add_player(john)
ghost.add_player(anna)
ghost.add_player(lisa)
ghost.add_player(karl)

# printing players cards at start
ghost.display_players()

# Start of the game
print('Welcome to bingo game')
# game flag
winner = False
# game loop
while winner is False:
    # choose number from game numbers
    current_number = random.choice(game_numbers)
    game_numbers.remove(current_number)

    # add it to list
    ghost.add_num(current_number)
    
    # delay
    time.sleep(1)

