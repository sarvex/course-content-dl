class SimpleGraph:
  def __init__(self, w=None, b=None):
    """Initializing the SimpleGraph

    Args:
      w (float): initial value for weight
      b (float): initial value for bias
    """
    if w is None:
      self.w = torch.randn(1, requires_grad=True)
    else:
      self.w = torch.tensor([w], requires_grad=True)
    if b is None:
      self.b = torch.randn(1, requires_grad=True)
    else:
      self.b = torch.tensor([b], requires_grad=True)

  def forward(self, x):
    """Forward pass

    Args:
      x (torch.Tensor): 1D tensor of features

    Returns:
      torch.Tensor: model predictions
    """
    assert isinstance(x, torch.Tensor)
    return torch.tanh(x * self.w + self.b)


def sq_loss(y_true, y_prediction):
  """L2 loss function

  Args:
    y_true (torch.Tensor): 1D tensor of target labels
    y_true (torch.Tensor): 1D tensor of predictions

  Returns:
    torch.Tensor: L2-loss (squared error)
  """
  assert isinstance(y_true, torch.Tensor)
  assert isinstance(y_prediction, torch.Tensor)
  return (y_true - y_prediction)**2


feature = torch.tensor([1])  # input tensor
target = torch.tensor([7])  # target tensor

simple_graph = SimpleGraph(-0.5, 0.5)
print(
    f"initial weight = {simple_graph.w.item()} \ninitial bias = {simple_graph.b.item()}"
)

prediction = simple_graph.forward(feature)
square_loss = sq_loss(target, prediction)

print(
    f"for x={feature.item()} and y={target.item()}, prediction={prediction.item()} and L2 Loss = {square_loss.item()}"
)