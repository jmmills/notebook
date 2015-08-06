from nose.tools import *
from pdb import set_trace


class Frame(object):
    def __init__(self, first=0, second=0):
        self.first = int(first)
        self.second = int(second)
        self.value = int(first) + int(second)
        self.__next = None
        self.__last = None

    @staticmethod
    def __valid_frame(self, frame=None):
        if frame:
            if not isinstance(frame, Frame):
                raise TypeError('frame must be an instance of Frame')

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, frame):
        self.__valid_frame(frame)
        self.__next = frame

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, frame):
        self.__valid_frame(frame)
        self.__last = frame

    def __int__(self):
        return self.score

    def __add__(self, other):
        return int(self) + int(other)

    @property
    def score(self):
        return self.value


class Strike(Frame):
    def __init__(self):
        first = 10
        super(self.__class__, self).__init__(first=first)

    @property
    def score(self):
        value = self.value

        if self.next and isinstance(self.next, Strike):
            value += self.next.value
            value += self.next.next.first
        elif self.next:
            value += self.next.value

        return value

class Spare(Frame):
    def __init__(self, first=0):
        second = 10 - int(first)
        super(self.__class__, self).__init__(first=first, second=second)

    @property
    def score(self):
        value = self.value

        if self.next:
            value += self.next.first

        return value



class Game(object):
    game_frames = 10

    def __init__(self):
        self.frames = []

    @property
    def current_frame(self):
        if self.frames:
            return self.frames[-1]
        else:
            return None

    def new_frame(self, first=0, second=0):
        frame = None

        if second == '/':
            frame = Spare(first=first)
        elif first == 'X' or second == 'X':
            frame = Strike()
        else:
            frame = Frame(first=first, second=second)

        if self.current_frame:
            self.current_frame.next = frame
            frame.last = self.current_frame

        self.frames.append(frame)

        return self

    @property
    def frame_scores(self):
        count = 0
        for frame in self.frames:
            if count < 10:
                count += 1
                yield frame.score

    @property
    def score(self):
        return sum(self.frame_scores)

    @classmethod
    def from_card(cls, card):
        game = Game()
        for n in card.split(' '):
            e = list(n)

            if len(e) == 1:
                e.append(0)

            game.new_frame(first=e[0], second=e[1])

        return game


def test_bad_game():
    game = Game.from_card('01 01 01 01 01 01 01 01 01 01')
    assert game.score == 10


def test_game_no_score_on_11th():
    game = Game.from_card('01 01 01 01 01 01 01 01 01 01 01')
    assert game.score == 10


def test_perfect_game():
    game = Game.from_card('X X X X X X X X X X X X X')
    assert game.score == 300


# http://goo.gl/G3OXVX
def test_example_game():
    game = Game.from_card('X 9/ 5/ 72 X X X 90 8/ 9/ X')
    assert game.score == 187