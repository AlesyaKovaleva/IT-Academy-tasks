from abc import ABC, abstractmethod


class Observable:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubcribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class SaveToFileObserver(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        if message == 'save':
            # save to file
            print(f'{self.__name} recieved!')


class Player(Observable):
    def set_team(self, team):
        self.team = team
        self.notify('save')


observer = SaveToFileObserver()

player = Player()
player.subscribe(observer)

player.set_team('Barcelona')
