class Multi_task_model(nn.Module):
  def __init__(self, pretrained=True, num_tasks=4, num_labels_per_task=[2, 2, 2, 5]):
    super(Multi_task_model, self).__init__()
    self.backbone = models.resnet18(pretrained=pretrained)                      # You can play around with different pre-trained models
    self.backbone = torch.nn.Sequential(*(list(self.backbone.children())[:-1])) # Remove the last fully connected layer

    if pretrained:
      for param in self.backbone.parameters():
        param.requires_grad = False

    self.fcs = []

    self.num_tasks = num_tasks

    self.fcs.extend(
        nn.Sequential(
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, num_labels_per_task[i]),
            ################################
            # Add more layers if you want! #
            ################################
            nn.Softmax(dim=1),
        ) for i in range(self.num_tasks))
    self.fcs_temp = nn.Sequential(*self.fcs)

  def forward(self, x):
    x = self.backbone(x)
    x = torch.flatten(x, 1)
    return [self.fcs[i](x) for i in range(self.num_tasks)]