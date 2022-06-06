from models import *


def play():
    print(RULES)
    user_name = input('Enter your name: ')
    while not user_name:
        user_name = input('Enter your name: ')
    choice = input('Enter start for start the game: ')
    while choice != 'start':
        choice = input('Enter start for start the game: ')
    player = Player(user_name)
    level = 1
    enemy = Enemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)

        except EnemyDown:
            player.score += 5
            level += 1
            enemy = Enemy(level)
        except GameOver:
            GameOver.get_scores(player.name, player.score)
            raise GameOver



if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    except GameOver:
        print('Error')
    finally:
        print('Good Bye')
