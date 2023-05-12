def epsilon_greedy(
    q_values_at_s: np.ndarray,  # Q-values in state s: Q(s, :).
    epsilon: float = 0.1  # Probability of taking a random action.
    ):
  """Return an epsilon-greedy action sample."""
  if epsilon < np.random.random():
    # Greedy: Pick action with the largest Q-value.
    return np.argmax(q_values_at_s)
  # Get the number of actions from the size of the given vector of Q-values.
  num_actions = np.array(q_values_at_s).shape[-1]
    # TODO else return a random action
  return np.random.randint(num_actions)