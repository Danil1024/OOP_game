from models import *


def get_player_instance():
    user_name = input('Enter your name: ')
    while not user_name:
        user_name = input('Enter your name: ')
    choice = input('Enter start for start the game: ')
    while choice != 'start':
        choice = input('Enter start for start the game: ')
    return Player(user_name)


def print_rules():
    print(RULES)


def get_enemy_instance(level=1):
    return Enemy(level)


def play():
    print_rules()
    player = get_player_instance()
    enemy = get_enemy_instance()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)

        except EnemyDown:
            player.score += 5
            enemy = get_enemy_instance(enemy.level + 1)
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
