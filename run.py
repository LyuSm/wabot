from yowsup.stacks import YowStackBuilder
from layer import EchoLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from consonance.structs.keypair import KeyPair
import base64


CREDENTIALS = ("79046438185", "mAWLq9Hma5tvf4eQfxKNc/XBNsszpXIz7cFcTG3qT2G8dRNAj8lD9WvqQ3ItrYFgaQ3doBIB4k0WkbH1F0j3AQ==") # replace with your phone and password


if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers()\
        .push(EchoLayer)\
        .build()

    stack.setCredentials(CREDENTIALS)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    stack.loop() #this is the program mainloop