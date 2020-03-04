
from pandas import DataFrame
from DBHelper import *

def getMatchesByCompetition(competitions):
    DBConnection = DBHelper()
    matches = DBConnection.fetch(
        ('SELECT matches.*, seasons.name as season_name FROM matches  '
         'JOIN seasons ON matches.season_id = seasons.season_id '
         'WHERE matches.competition_id IN (%s) and matches.status = 8' % ','.join([
             '%s'] * len(competitions))
         ), competitions
    )

    df = DataFrame(matches)
    df = df.drop(columns=['status', 'start_time',
                          'home_extend', 'home_penalty', 'away_extend',
                          'away_penalty', 'match_description', 'ground',
                          'animation', 'live_streaming', 'detail', 'lineup',
                          'analysis', 'intelligence', 'index', 'europe_index',
                          'stage_id', 'round_num', 'group_num', 'created_at', 'updated_at'])

    df.to_csv('matches.csv')  # 相对位置


if __name__ == '__main__':
    competitions = [82, 108, 120, 129, 142]
    getMatchesByCompetition(competitions)
