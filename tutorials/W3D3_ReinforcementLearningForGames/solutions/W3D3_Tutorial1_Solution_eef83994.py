class PolicyBasedPlayer():
  def __init__(self, game, pnet, greedy=True):
    self.game = game
    self.pnet = pnet
    self.greedy = greedy

  def play(self, board):
    valids = self.game.getValidMoves(board, 1)
    action_probs = self.pnet.predict(board)
    vap = action_probs*valids  # masking invalid moves
    sum_vap = np.sum(vap)

    if sum_vap > 0:
      vap /= sum_vap  # renormalize
    else:
      # if all valid moves were masked we make all valid moves equally probable
      print("All valid moves were masked, doing a workaround.")
      vap = vap + valids
      vap /= np.sum(vap)

    return (np.where(vap == np.max(vap))[0][0] if self.greedy else
            np.random.choice(self.game.getActionSize(), p=vap))


# playing games
num_games = 20
player1 = PolicyBasedPlayer(game, pnet, greedy=True).play
player2 = RandomPlayer(game).play
arena = Arena.Arena(player1, player2, game, display=OthelloGame.display)
## Uncomment below to test!
result = arena.playGames(num_games, verbose=False)
print(result)