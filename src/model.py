import utils

class Model:
    data = None
    def __init__(self):
        utils.printHeader("Initializing model")
    
    def train(self):
        utils.printHeader("Training mode")
    
    def inference(self):
        utils.printHeader("Inference mode")
    
    def loadData(self, data):
        self.data = data