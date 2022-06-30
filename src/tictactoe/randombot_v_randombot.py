from ttt.player import Player
from ttt.game import Game
from ttt.random_bot import RandomBot

def main():
    xbot = RandomBot(Player.x)
    obot = RandomBot(Player.o)
    game = Game(1000)
    game.simulate(xbot, obot)

if __name__ == '__main__':
    main()