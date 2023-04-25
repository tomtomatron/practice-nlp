import os
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch import nn, utils 
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger

from model import Tomcoder

def main():
    wandb_logger = WandbLogger(project="practice-nlp")
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    model = Tomcoder(encoder, decoder, lr=0.001) 
    dataset = MNIST(os.getcwd(), download=True, transform=ToTensor())
    train_loader = utils.data.DataLoader(dataset, num_workers=16, batch_size=4096)
    trainer = pl.Trainer(logger=wandb_logger, accelerator="cpu", max_epochs=1)
    trainer.fit(model=model, train_dataloaders=train_loader)


if __name__ == "__main__":
    main()