#TODO: Import packages you need

def train(model, train_loader, cost, optimizer, epoch):
    model.train()
    #TODO: Add your code here to train your model
    pass

def test(model, test_loader):
    model.eval()
    #TODO: Add code here to test the accuracy of your model
    pass

def create_model():
    #TODO: Add your model code here. You can use code from previous exercises
    return model

#TODO: Create your Data Transforms

#TODO: Download and create loaders for your data

model=create_model()

cost = #TODO: Add your cost function here. You can use code from previous exercises

optimizer = #TODO: Add your optimizer here. You can use code from previous exercises


train(model, train_loader, cost, optimizer, epoch)
test(model, test_loader)
