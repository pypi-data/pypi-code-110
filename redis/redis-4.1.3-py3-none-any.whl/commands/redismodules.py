from json import JSONDecoder, JSONEncoder


class RedisModuleCommands:
    """This class contains the wrapper functions to bring supported redis
    modules into the command namepsace.
    """

    def json(self, encoder=JSONEncoder(), decoder=JSONDecoder()):
        """Access the json namespace, providing support for redis json."""

        from .json import JSON

        jj = JSON(client=self, encoder=encoder, decoder=decoder)
        return jj

    def ft(self, index_name="idx"):
        """Access the search namespace, providing support for redis search."""

        from .search import Search

        s = Search(client=self, index_name=index_name)
        return s

    def ts(self):
        """Access the timeseries namespace, providing support for
        redis timeseries data.
        """

        from .timeseries import TimeSeries

        s = TimeSeries(client=self)
        return s

    def bf(self):
        """Access the bloom namespace."""

        from .bf import BFBloom

        bf = BFBloom(client=self)
        return bf

    def cf(self):
        """Access the bloom namespace."""

        from .bf import CFBloom

        cf = CFBloom(client=self)
        return cf

    def cms(self):
        """Access the bloom namespace."""

        from .bf import CMSBloom

        cms = CMSBloom(client=self)
        return cms

    def topk(self):
        """Access the bloom namespace."""

        from .bf import TOPKBloom

        topk = TOPKBloom(client=self)
        return topk

    def tdigest(self):
        """Access the bloom namespace."""

        from .bf import TDigestBloom

        tdigest = TDigestBloom(client=self)
        return tdigest

    def graph(self, index_name="idx"):
        """Access the timeseries namespace, providing support for
        redis timeseries data.
        """

        from .graph import Graph

        g = Graph(client=self, name=index_name)
        return g
