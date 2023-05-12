class NeuralNet(nn.Module):
  def __init__(self, batch_size, output_size, hidden_size, vocab_size, embedding_length, word_embeddings):
    super(NeuralNet, self).__init__()

    self.batch_size = batch_size
    self.output_size = output_size
    self.hidden_size = hidden_size
    self.vocab_size = vocab_size
    self.embedding_length = embedding_length

    self.word_embeddings = nn.Embedding(vocab_size, embedding_length)
    self.word_embeddings.weight = nn.Parameter(word_embeddings, requires_grad=False)
    self.fc1 = nn.Linear(embedding_length, hidden_size)
    self.fc2 = nn.Linear(hidden_size, output_size)


  def forward(self, inputs):

    input = self.word_embeddings(inputs)  # convert text to embeddings
    # Average the word embedddings in a sentence
    # Use torch.nn.functional.avg_pool2d to compute the averages
    pooled = F.avg_pool2d(input, (input.shape[1], 1)).squeeze(1)

    # Pass the embeddings through the neural net
    # A fully-connected layer
    x = self.fc1(pooled)
    # ReLU activation
    x = F.relu(x)
    # Another fully-connected layer
    x = self.fc2(x)
    return F.log_softmax(x, dim=1)


# Uncomment to check your code
nn_model = NeuralNet(32, 2, 128, 100, 300, TEXT.vocab.vectors)
print(nn_model)