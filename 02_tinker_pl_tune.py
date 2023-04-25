import os
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch import nn
import pytorch_lightning as pl

from model import Tomcoder


def main():
    encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
    decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))
    model = Tomcoder(encoder, decoder) 
    trainer = pl.Trainer(accelerator="gpu", devices=1, max_epochs=1)
    trainer.tune(model)
    print(model.lr)

if __name__ == "__main__":
    main()
