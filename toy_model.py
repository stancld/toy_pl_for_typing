import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl


class ToyModel(pl.LightningDataModule):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(10, 25),
            nn.ReLU(),
            nn.Linear(25, 1),
        )

    def forward(self, x):
        pred = self.model(x)
        return pred

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self.forward(x.view(-1))
        loss = F.mse_loss(y_pred, y)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self.forward(x.view(-1))
        loss = F.mse_loss(y_pred, y)
        self.log("val_loss", loss)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer
