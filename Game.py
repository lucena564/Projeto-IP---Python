from GamePlay import GamePlay

class Game:
    def __init__(self):
        self.__game_play = GamePlay()

    def load(self):
      self.__game_play()

if __name__ == "__main__":
    Game().load()