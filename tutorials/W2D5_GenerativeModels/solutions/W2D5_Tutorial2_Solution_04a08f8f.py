def loss_gen(disc, x_fake):
  """Compute the generator loss for `x_fake` given `disc`

  Args:
    disc: The generator
    x_fake (ndarray): An array of shape (N,) that contains the fake samples

  Returns:
    ndarray: The generator loss
  """

  # Loss for fake data
  label_fake = 1
  return label_fake * torch.log(disc.classify(x_fake))


disc = DummyDisc()
gen = DummyGen()

x_fake = gen.sample()
## Uncomment below to check your function
lg = loss_gen(disc, x_fake)
with plt.xkcd():
  plotting_lg(lg)