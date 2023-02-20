import os
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch import optim, nn, utils, Tensor
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger


class Tomcoder(pl.LightningModule):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

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
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer




def main():
    wandb_logger = WandbLogger(project="practice-nlp")
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    tomcoder = Tomcoder(encoder, decoder) 

    dataset = MNIST(os.getcwd(), download=True, transform=ToTensor())
    train_loader = utils.data.DataLoader(dataset)

    trainer = pl.Trainer(logger=wandb_logger)
    trainer.fit(model=tomcoder, train_dataloaders=train_loader)

    for i in range(10):
        wandb_logger.watch


if __name__ == "__main__":
    main()