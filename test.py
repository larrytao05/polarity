import WebSocket


def onWelcome(Content):
    print("WELCOMED")


WebSocket.bindToEvent("WelcomeEvent", onWelcome)

WebSocket.send({
    "className": "HiEvent"
})


# WebSocket.close()

