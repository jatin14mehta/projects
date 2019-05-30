from random import randint
import time


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(4, 9)


track1 = Track('baby')
track2 = Track('uproar')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class NodeQueue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        current = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        return current


class MediaPlayerQueue(NodeQueue):
    def __init__(self):

        NodeQueue.__init__(self)

    def addTrack(self, track):

        self.enqueue(track)

    def play(self):
        while self.size > 0:
            current_track = self.dequeue()
            print(f"current_track : {current_track.data.title}")
            time.sleep(current_track.data.length)


mediaPlayer1 = MediaPlayerQueue()
mediaPlayer1.addTrack(track1)
mediaPlayer1.addTrack(track2)
mediaPlayer1.play()
