import WebSocket


def onWelcome(Content):
    print("WELCOMED")


def recivedMessage(Content):
    print(Content["sender"]+": "+Content["message"])


def sendChat(Message):
    print("You: " + Message)
    WebSocket.send({
        "className": "SendMessageEvent",
        "sender": "user2",
        "message": "Hello, world!"
    })


def onJoinedRoom(Content):
    print("You joined a room!")
    sendChat("Hello, friend!")


WebSocket.bindToEvent("WelcomeEvent", onWelcome)
WebSocket.bindToEvent("ReceiveMessageEvent", recivedMessage)
WebSocket.bindToEvent("JoinedRoomEvent", onJoinedRoom)

WebSocket.send({
    "className": "SetPreferenceEvent",
    "topic": "testTopic",
    "preference": -2,
})
WebSocket.send({
    "className": "StartChatEvent",
    "topic": "testTopic",
})

# WebSocket.close()

