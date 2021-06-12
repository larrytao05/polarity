import asyncio
import json
import socket
from threading import Thread

Address = ("localhost", 16568)
HeaderSize = 10
WebSocket = socket.socket()
Running = True
Binds = {}

class myThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            try:
                Header = WebSocket.recv(10)
                if not Header:
                    break
                MessageLength = int(Header[:Header.index(b'-')])

                Content = WebSocket.recv(MessageLength)
                Content = Content.decode('utf-8')
                Content = json.loads(Content)

                if Binds[Content["className"]]:
                    Binds[Content["className"]](Content)

            except OSError:
                break


IncomingThread = myThread()


def covertToJson(dictionary):
    return json.dumps(dictionary)


def bindToEvent(EventName, Function):
    Binds[EventName] = Function


def formatForSending(Text):
    Header = str(len(Text))
    Header = Header + ("-" * (HeaderSize - len(Header)))

    CombinedText = Header + Text

    return CombinedText.encode('utf-8')


async def sendAysnc(Dictionary):
    Text = covertToJson(Dictionary)
    FormattedMessage = formatForSending(Text)

    print(FormattedMessage)
    WebSocket.send(FormattedMessage)


def send(Dictionary):
    asyncio.get_event_loop().run_until_complete(sendAysnc(Dictionary))


def connect():
    WebSocket.connect(Address)
    IncomingThread.start()


def close():
    WebSocket.close()

# Main
connect()