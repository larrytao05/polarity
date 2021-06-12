import asyncio
import json
import socket
from threading import Thread

Address = ("localhost", 16568)
Headersize = 10
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
    Header = Header + ("-" * (Headersize - len(Header)))

    CombinedText = Header + Text

    return CombinedText.encode('utf-8')


async def sendAysnc(Dictionary):
    Text = covertToJson(Dictionary)
    FormatedMessage = formatForSending(Text)

    print(FormatedMessage)
    WebSocket.send(FormatedMessage)


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


def send(Dictionary):
    get_or_create_eventloop().run_until_complete(sendAysnc(Dictionary))


def connect():
    WebSocket.connect(Address)
    IncomingThread.start()


def close():
    WebSocket.close()


connect()