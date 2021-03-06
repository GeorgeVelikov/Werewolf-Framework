import Shared.constants.NetConstants as NetConstants;
import Shared.utility.DateTimeUtility as DateTimeUtility

from datetime import datetime;

class MessageDto():
    def __init__(self, author, text):
        self.__timeUtc = datetime.utcnow();
        self.__author = author;
        self.__text = text;

    def __str__(self):
        return self.TimeStampLocal + " " + self.Content;

    def __repr__(self):
        return str(self);

    @property
    def Author(self):
        if self.__author:
            return self.__author;

        return "[SERVER]";

    @property
    def TimeUtc(self):
        return self.__timeUtc;

    @property
    def TimeStampUtc(self):
        return self.__timeUtc\
            .strftime(NetConstants.DATETIME_FORMAT);

    @property
    def TimeStampLocal(self):
        return DateTimeUtility.UtcToLocal(self.__timeUtc)\
            .strftime(NetConstants.TIME_FORMAT);

    @property
    def AuthorIdentifier(self):
        if not self.__author:
            return self.Author;

        return self.__author.Identifier;

    @property
    def AuthorName(self):
        if not self.__author:
            return self.Author;

        return self.__author.Name;

    @property
    def Text(self):
        return self.__text;

    @property
    def Content(self):
        return self.AuthorName + " " + ("says: " if self.__author else str()) + self.Text;
