from players.player import Player


class BasicPlayer(Player):
    """ Basic Player - Plays pass line with 2x odds.\nDefault: Places (6, 8)."""

    def __init__(self, bankroll=500):
        super(BasicPlayer, self).__init__(bankroll)
        print BasicPlayer.__doc__

    @staticmethod
    def strategy(table):
        if table.point is None:
            table.bet.make_pass_bet(table, table.minimum)
        elif table.bet.comeOdds[table.point][1] == 0:
            table.bet.establish_pass_odds(table, table.minimum * 2)
            # table.bet.make_across_place_bet(table, table.minimum)
            table.bet.make_place_bet(6, table, table.minimum)
            table.bet.make_place_bet(8, table, table.minimum)
        else:
            # table.bet.make_across_place_bet(table, table.minimum)
            table.bet.make_place_bet(6, table, table.minimum)
            table.bet.make_place_bet(8, table, table.minimum)

    @staticmethod
    def get_wager(bet):
        wager = bet.get_wager()
        come = 'C' + str([k for k, v in bet.comeOdds.iteritems() if v[0]])
        place = 'P' + str([k for k, v in bet.place.iteritems() if v])
        wager = " ".join((str(wager), str(come), str(place)))
        return wager

    @staticmethod
    def get_odds(number, amount):
        if number in (4, 5, 6, 8, 9, 10):
            return 2 * amount
