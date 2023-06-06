# Topic - consumer
from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):

    '''This handler is called when client initially opens a connection
    and is about to finish the websocket handshake. '''

    def websocket_connect(self, event):
        print('websocket connected........')
    
    '''This handler is called when data received from client. '''

    def websocket_receive(self, event):
        print('Message received.......')
    
    '''This handler is called when either connection to the client is lost,
    either from the client closing the connection. The server closing the
    connection or loss the socket.'''

    def websocket_disconnect(self, event):
        print('websocket disconnected.......')


class MyAsyncConsumer(AsyncConsumer):

    '''This handler is called when client initially opens a connection
    and is about to finish the websocket handshake. '''

    async def websocket_connect(self, event):
        print('websocket connected........')
    
    '''This handler is called when data received from client. '''

    async def websocket_receive(self, event):
        print('Message received.......')
    
    '''This handler is called when either connection to the client is lost,
    either from the client closing the connection. The server closing the
    connection or loss the socket.'''

    async def websocket_disconnect(self, event):
        print('websocket disconnected.......')