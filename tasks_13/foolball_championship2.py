from abc import ABC, abstractmethod
# import json
import time
# import os
import uuid


class Observable:
    def __init__(self):
        self._subscribers = set()

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubcribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, obj, message):
        for subscriber in self._subscribers:
            subscriber.update(obj, message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, obj, message):
        pass


class SaveToFileObserver(AbstractObserver):
    def update(self, obj, message):
        if message == 'save_player':
            pass


class Team(Observable):
    all_teams = []

    def __init__(self, name):
        self._uid = uuid.uuid4()
        self._name = name
        self._players = []
        Team.all_teams.append(self)

    def add_player(self, player):
        if player._team is None:
            self._players.append(player)
            player._team = self
        else:
            print(
                f'Невозможно добавить игрока в команду, '
                f'т.к. он игрок команды {player._team}'
            )

    def delete_player(self, player):
        if player in self._players:
            self._players.remove(player)
            player._team = None
        else:
            print(
                f'{player._name} не является игроком команды {self._name}'
            )

    @property
    def all_players(self):
        return self._players if self._players else 'В команде нет игроков.'

    def __repr__(self):
        return f'{self._name}'

    def __str__(self):
        return f'{self._name}'


class Player(Observable):
    all_players = []

    def __init__(self, name, team=None):
        self._uid = uuid.uuid4()
        self._name = name
        self._team = team
        Player.all_players.append(self)
        if self._team is not None:
            if self._team in team.all_teams:
                team._players.append(self)
            else:
                print('Такой команды не существует!')
    
    # def get_team(self):
    #     if not self._team_id:
    #         return None
        
    #     p_team = filter(lambda team: team.id == self._team_id, Team.all_teams)

    #     return team

    def delete(self):
        if self._team is not None:
            self._team._players.remove(self)
            self._team = None
        self.all_players.remove(self)
        del self

    def set_team(self, team):
        if self._team is None:
            if team in team.all_teams:
                self._team = team
                team._players.append(self)
            else:
                print('Такой команды не существует.')
        else:
            print(
                f'Невозможно поменять команду, т.к. '
                f'игрок состоит в команде {self._team}'
            )

    @property
    def team(self):
        if self._team is None:
            return 'У этого игрока нет команды!'
        else:
            return f'{self._name} игрок команды {self._team}.'

    def __str__(self):
        return f'{self._name}'

    def __repr__(self):
        return f'{self._name}'


class Match:
    def __init__(self, data, location, team1, team2):
        self.uid = uuid.uuid4()
        self.data = valid_date(data)
        self.location = location
        self.team1 = team1
        self.team2 = team2

# id, date, location, result, team1, team2, players


def valid_date(date):
    try:
        valid_date = time.strptime(date, '%d/%m/%Y')
        return f'{valid_date[2]}.{valid_date[1]}.{valid_date[0]}'
    except ValueError:
        return None


def save_to_file(file, obj):
    # player_json = json.dumps(obj)
            # if not os.path.isfile('players.json'):
            #     with open('players.json', 'w') as f:
            #         f.write(player_json)

            # with open('players.json', 'r', encoding='utf-8') as data:
            #     players_j = json.load(data)
            #     print(players_j)

            # with open('players.json', 'w', encoding='utf-8') as data:
    pass


observer = SaveToFileObserver()

first_team = Team('First')
second_team = Team('Second')
third_team = Team('Third')

player1 = Player('Papa Carlo', first_team)

player2 = Player('Mama Darlo', second_team)

player3 = Player('Bla Bla')

match1 = Match('01/06/1986', 'Minsk', first_team, second_team)
print(match1.data)

