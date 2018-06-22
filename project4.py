'''
created by soviv 6222018
'''
import csv
def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    table = []
    for dic in statistics:
        if dic[yearid] == str(year):
            table.append(dic)
    return table


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    table = []
    for dic in statistics:
        table.append((dic[info['playerid']], formula(info, dic)))

    table = sorted(table, key=lambda x: x[1], reverse=True)
    return table[0:numplayers]

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []

    with open(filename, 'r') as csv_file:
        csv_file = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        for line in csv_file:
            table.append(line)
    return table

def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    m_stat = read_csv_as_list_dict(info['masterfile'], info['separator'], info['quote'])
    table = []
    for ids in top_ids_and_stats:
        for dit in m_stat:
            if dit[info['playerid']] == ids[0]:
                table.append('{0:.3f} --- {1} {2}'.format(ids[1], dit[info['firstname']], dit[info['lastname']]))
    return table

def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and 
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to compute top statistics for
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    b_stat = read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote'])

    # year = 2020
    # formula = batting_average
    # numplayers = 3

    sep_year = filter_by_year(b_stat, year, info['yearid'])

    top_player = top_player_ids(info, sep_year, formula, numplayers)

    player_name = lookup_player_names(info, top_player)

    return player_name


def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    dictt = {}

    for dit in statistics:
        dictt[dit[playerid]] = {}
        for field in fields:
            dictt[dit[playerid]][field] = 0
            dictt[dit[playerid]][playerid] = dit[playerid]

    # Everything is set up, only addition of fields is due:
    #print(d)

    for key, val in dictt.items():
        for dit in statistics:
            if key == dit[playerid]:
                # print(True)
                for stat in fields:
                    dictt[key][stat] += int(dit[stat])
    return dictt


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and 
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    bat_stat = read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote'])

    fieldnames = info['battingfields']

    # numplayers = 4

    indiv_player_stat = aggregate_by_player_id(bat_stat, info['playerid'], fieldnames)

    # print(indiv_player_stat)

    # separate player names from aggregate by player ID:

    player_name = [k for k, v in indiv_player_stat.items()]

    # print(player_name)

    # compunded stats for each player:

    compounded_stat = []

    for player in player_name:
        compounded_stat.append((player, formula(info, indiv_player_stat[player])))

    # Sort the compounded stat:

    # print(compounded_stat)

    # now look up player names:

    compounded_stat = sorted(compounded_stat, key=lambda x: x[1], reverse=True)

    return lookup_player_names(info, compounded_stat[0:numplayers])
