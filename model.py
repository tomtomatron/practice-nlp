from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch import optim, nn, utils, Tensor
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger


class Tomcoder(pl.LightningModule):
    def __init__(self, encoder, decoder, batch_size=32, lr=1e-3):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.batch_size = batch_size
        self.lr = lr

    def training_step(self, batch, batch_idx):
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat, x)
        self.log("train/loss", loss)
        self.save_hyperparameters()
        return loss

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=self.lr)
        return optimizer