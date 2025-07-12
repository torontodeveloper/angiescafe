from fastapi import FastAPI
from databaseSetup import run,read_orders

app = FastAPI()
run()

readOrderQuery = 'SELECT * FROM item'

@app.get('/orders')
def fetchListOfOrder():
    '''
    Returns List ofOrders
    '''
    orders = read_orders(readOrderQuery)
    print('Fetch Order',type(orders))
    for order in orders:
        print(f'order is {order}')
    return orders

@app.post('/newOrder')
def orderItem():
    '''
     Places an Order
    '''
    pass

@app.post('/orders/{orderId}/cancelOrder')
def orderItem():
    '''
    Cancels an Order
    '''
    pass

