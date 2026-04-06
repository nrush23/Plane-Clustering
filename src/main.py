from model import Model
from dataloader import DataLoader
def main():
    model = Model()
    dataLoader = DataLoader()
    data = dataLoader.getData()
    model.train()

    model.inference()
if __name__ == '__main__':
    main()