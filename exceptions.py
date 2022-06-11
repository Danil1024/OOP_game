class GameOver(Exception):

	@staticmethod
	def get_scores(player_name, player_score):
		with open('scores.txt', 'a') as score:
			score.write(f'Player - {player_name}, scored: {player_score} points\n')


class EnemyDown(Exception):
	pass

