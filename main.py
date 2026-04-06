from model import Model

def main():
    model = Model()
    model.train()

    model.inference()
if __name__ == '__main__':
    main()