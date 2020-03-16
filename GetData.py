
from pandas import DataFrame
from DBHelper import *


def getMatchesByCompetition(competitionId):
    DBConnection = DBHelper()
    matches = DBConnection.fetch(
        ('SELECT '
            'matches.match_id, '
            'matches.status, '
            'matches.competition_id, '
            'matches.open_date, '
            'matches.home_team, '
            'matches.away_team, '
            'matches.home_rank, '
            'matches.home_score, '
            'matches.home_half_score, '
            'matches.home_red, '
            'matches.home_yellow, '
            'matches.home_corner away_rank, '
            'matches.away_score, '
            'matches.away_half_score, '
            'matches.away_red, '
            'matches.away_yellow, '
            'matches.away_corner '
         'FROM '
            'matches '
         'JOIN seasons ON matches.season_id = seasons.season_id '
         'WHERE matches.competition_id = %s'
         ), competitionId
    )

    df = DataFrame(matches)
    df.to_csv('data/' + str(competitionId) + '/matches.csv')  # 相對位置


def getTeamsByCompetition(competitionId):
    DBConnection = DBHelper()
    teams = DBConnection.fetch(
        'SELECT '
        'team_id, '
        'competition_id, '
        'short_name_zh, '
        'short_name_en, '
        'market_value '
        'FROM '
            'teams '
        'WHERE '
            'competition_id = %s'
        , competitionId
    )

    df = DataFrame(teams)
    df.to_csv('data/' + str(competitionId) + '/teams.csv')  # 相對位置

def getIntelligenceByCompetition(competitionId):
    DBConnection = DBHelper()
    info = DBConnection.fetch(
        'SELECT '
            'info.match_id, '
            'info.info_type, '
            'info.team_info, '
            'info.level '
        'FROM '
            'intelligence_info as info '
        'JOIN matches ON matches.match_id = info.match_id '
        'WHERE '
            'matches.competition_id = %s AND info.info_type != 3'
        , competitionId
    )
    infoDF = DataFrame(info)
    infoDF.to_csv('data/' + str(competitionId) + '/info.csv')  # 相對位置

    similar = DBConnection.fetch(
        'SELECT '
            'similar.match_id, '
            'similar.match_count, '
            'similar.model_count, '
            'similar.change_count, '
            'similar.league_count, '
            'similar.won, '
            'similar.drawn, '
            'similar.lost '
        'FROM '
            'intelligence_similar as similar '
        'JOIN matches ON matches.match_id = similar.match_id '
        'WHERE '
            'matches.competition_id = %s'
        , competitionId
    )

    similarDF = DataFrame(similar)
    similarDF.to_csv('data/' + str(competitionId) + '/similar.csv')  # 相對位置

    change = DBConnection.fetch(
        'SELECT  '
            'chance.match_id, '
            'chance.type, '
            'chance.team_info, '
            'chance.won_count, '
            'chance.drawn_count, '
            'chance.lost_count, '
            'chance.rate '
        'FROM '
            'intelligence_chance as chance '
        'JOIN matches ON matches.match_id = chance.match_id '
        'WHERE '
            'matches.competition_id = %s'
        , competitionId
    )

    changeDF = DataFrame(change)
    changeDF.to_csv('data/' + str(competitionId) + '/change.csv')  # 相對位置

if __name__ == '__main__':
    getMatchesByCompetition(82)
    getTeamsByCompetition(82)
    getIntelligenceByCompetition(82)
