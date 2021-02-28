import Shared.constants.GameConstants as GameConstants;
import Shared.utility.LogUtility as LogUtility;
from Shared.enums.TimeOfDayEnum import TimeOfDayEnum;
from Shared.exceptions.GameException import GameException;

import Werewolf.game.GameRules as GameRules;

from Werewolf.agents.AgentPlayer import AgentPlayer;

import uuid;
from collections import Counter;

class Game():
    def __init__(self, name):
        self.__identifier = uuid.uuid4().hex;
        self.__hasStarted = False;
        self.__name = name;
        self.__messages = set();
        self.__votes = set();
        self.__turn = int();
        self.__players = set();
        self.__timeOfDay = TimeOfDayEnum._None;

    def __str__(self):
        return self.Name + " - " + self.Identifier;

    def __repr__(self):
        return self.Name + " - " + self.Identifier;

    #region properties

    @property
    def Name(self):
        return self.__name;

    @property
    def Identifier(self):
        return self.__identifier;

    @property
    def HasStarted(self):
        return self.__hasStarted;

    @property
    def Name(self):
        return self.__name;

    @property
    def Messages(self):
        return self.__messages;

    @property
    def Votes(self):
        return self.__votes;

    @property
    def Turn(self):
        return self.__turn;

    @property
    def Players(self):
        return sorted(self.__players,\
            key = lambda p: p.Name, \
            reverse = False);

    @property
    def PlayerIdentifiers(self):
        return [p.Identifier for p in self.__players];

    @property
    def TimeOfDay(self):
        return self.__timeOfDay;

    @property
    def HasAgentPlayers(self):
        return any(player for player in self.__players \
            if issubclass(type(player), AgentPlayer));

    @property
    def AgentPlayers(self):
        return [player for player in self.__players \
            if issubclass(type(player), AgentPlayer)];

    #endregion

    #region Game calls

    def Join(self, player):
        self.__players.add(player);
        return;

    def Leave(self, player):
        if (player.Identifier not in self.PlayerIdentifiers):
            print(f"[ERROR] Player {player.Identifier} is not in the game.");
            # TODO: raise some silent exception
            return;

        # no need to sort, already alphabetical
        self.__players\
            .remove(self.GetPlayerByIdentifier(player.Identifier));

    def Start(self):
        if (len(self.__players) < GameConstants.MINIMAL_PLAYER_COUNT):
            print(f"[ERROR] Cannot start game without having at least {GameConstants.MINIMAL_PLAYER_COUNT} players.");
            return;

        for player in self.__players:
            player._Player__isReady = False;

        GameRules.DistributeRolesBaseGame(self.__players);

        self.__hasStarted = True;
        self.__votes = set();
        self.__turn = 1;
        self.__timeOfDay == TimeOfDayEnum.Day;

        for agent in self.AgentPlayers:
            agent.ActDay();

        return;

    def Restart(self):
        for player in self.__players:
            player._Player__isReady = False;
            player._Player__role = None;

        self.__hasStarted = False;
        self.__votes = set();
        self.__turn = int();
        self.__timeOfDay = TimeOfDayEnum._None;

    def VoteStart(self, player):
        if not player:
            return;

        player._Player__isReady = not player._Player__isReady;

        isThereAnyNonReadyPlayers = any(p for p in self.__players if not p.IsReady);

        if isThereAnyNonReadyPlayers:
            return;

        self.Start();

        return;

    def Vote(self, vote):
        if not vote:
            return;

        playerIdentifiers = self.PlayerIdentifiers;

        if not vote.Player.Identifier in playerIdentifiers or\
            not vote.VotedPlayer.Identifier in playerIdentifiers:
            # players not in the game, error
            print("Invalid vote, one of the players is not in the game");
            return;

        self.Votes.add(vote);
        print(f"{vote.Player.Name} votes to kill {vote.VotedPlayer.Name}");

        if len(self.Votes) == len(playerIdentifiers):
            self.CountVotes();

        return;

    def CountVotes(self):
        votedPlayerIdentifiers = [vote.VotedPlayer.Identifier for vote in self.__votes];
        counter = Counter(votedPlayerIdentifiers);

        (mostVotedPlayerIdentifier, times) = counter.most_common(1)[0];

        playerToExecute = self.GetPlayerByIdentifier(mostVotedPlayerIdentifier);

        LogUtility.CreateGameMessage(f"{playerToExecute.Name} has the most votes to get executed - {times}.", self);

        self.Execute(playerToExecute);
        self.__votes = set();
        return;

    def Execute(self, player):
        if player not in self.Players:
            return;

        player._Player__isAlive = False;
        LogUtility.CreateGameMessage(f"{player.Name} is executed.", self);

        return;

    #endregion

    #region Helpers

    def GetPlayerByIdentifier(self, playerIdentifier):
        return next((p for p in self.__players\
            if p.Identifier == playerIdentifier), None);

    def HasPlayerVotedAlready(self, playerIdentifier):
        return any(v for v in self.__votes \
            if v.Player.Identifier == playerIdentifier);

    #endregion
