""" CSC108 Assignment 3: Social Networks - Starter code """  # Ignore QuotesBear
from typing import List, Tuple, Dict, TextIO


def count_profiles(profiles_file: TextIO) -> int:
    """Count the "number of profiles" in the file

    Docstring examples not given since result depends on input data.
    """
    count = 0
    for line in profiles_file:
        if line.strip() == '':
            count += 1
    profiles_file.seek(0)
    return count + 1


def format_name(name: str) -> str:
    """Format the name as "Firstname(s) + Lastnames"

    example: "Pritchett, Jay" converts to "Jay Pritchett"
    """
    return name.split(',')[1][1:] + ' ' + name.split(',')[0]


def format_list(list_: List[str]) -> List[str]:
    """Remove duplicate items from the list and sorts the list in
    alphabetic order of names present in the list

    :param list_: the unformatted list
    :return: the formatted list

    example: ['Gloria Pritchett','Manny Delgado','Claire Dunphy','Claire Dunphy']
    converts to
    ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado']
    """
    set_ = set(list_)
    formatted_list = list(set_)
    formatted_list.sort()
    return formatted_list


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]],
                  person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    number_of_profiles = count_profiles(profiles_file)
    for _ in range(number_of_profiles):
        person_name = format_name(str(profiles_file.readline().strip()))
        list_of_networks, list_of_friends = [], []
        line = profiles_file.readline().strip()
        while line != '':
            if ',' not in line:
                list_of_networks.append(str(line))
            else:
                list_of_friends.append(format_name(str(line)))
            line = profiles_file.readline().strip()
        if format_list(list_of_friends) != list():
            person_to_friends[person_name] = format_list(list_of_friends)
        if format_list(list_of_friends) != list():
            person_to_networks[person_name] = format_list(list_of_networks)


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Count the average number of friends that people who appear as keys in the
    "person to friends" dictionary have.

    example: {'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker':
    ['Gloria Pritchett','Mitchell Pritchett']} returns 1.5
    """
    num_friend_list = []  # list of number of friends for each key in dictionary

    for key in person_to_friends:
        num_friend_list.append(len(person_to_friends[key]))

    if num_friend_list == list():
        return 0
    else:
        return sum(num_friend_list) / len(num_friend_list)


def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary based on the given
    "person to friends" dictionary.

    example: {'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker':
    ['Gloria Pritchett','Mitchell Pritchett']} returns {'Dunphy': ['Alex', 'Luke'],
     'Tucker': ['Cameron'],'Pritchett': ['Gloria', 'Mitchell']}
    """
    list_of_people = [key for key in person_to_friends]
    for key in person_to_friends:
        for names in person_to_friends[key]:
            list_of_people.append(names)
    list_of_people = format_list(list_of_people)
    dict_fam_mem = {}  # Required Dictionary
    for name in list_of_people:
        last_name = name.split(' ')[-1]
        list_fam_mem = []  # List containing the first name of family members
        for member in list_of_people:
            if member.split(' ')[-1] == last_name:
                first_name_list = member.split(' ')[:-1]
                list_fam_mem.append(' '.join(first_name_list))
        dict_fam_mem[last_name] = list_fam_mem
    return dict_fam_mem


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "network to people" dictionary based on the given
    "person to networks" dictionary.

    example: {'Manny Delgado': ['Chess Club'],'Alex Dunphy': ['Chess Club',
    'Orchestra']} returns {'Chess Club': ['Alex Dunphy', 'Manny Delgado'],
    'Orchestra': ['Alex Dunphy']}
    """
    list_of_networks = [x for key in person_to_networks
                        for x in person_to_networks[key]]

    dict_of_network = {}

    for network in list_of_networks:
        list_of_names = []
        for key in person_to_networks:
            if network in person_to_networks[key]:
                list_of_names.append(key)
        dict_of_network[network] = format_list(list_of_names)

    return dict_of_network


def get_friends_of_friends(person_to_friends: Dict[str, List[str]],
                           person: str) -> List[str]:
    """Return the list of names of people who are friends of friends of the
    "person" by making use of "person_to_friends" dictionary.

    example: {'Jay Pritchett': ['Claire Dunphy'], 'Claire Dunphy':
    ['Jay Pritchett','Mitchell Pritchett', 'Phil Dunphy']} returns
    ['Mitchell Pritchett', 'Phil Dunphy']
    """
    list_far_frnds = []  # list of friends of friends
    for friend in person_to_friends[person]:
        if friend in person_to_friends:
            for friend_of_friend in person_to_friends[friend]:
                if friend_of_friend not in person_to_friends[person] and person \
                        not in person_to_friends[person]:
                    list_far_frnds.append(friend_of_friend)

    list_far_frnds = [friend_of_friend for friend_of_friend in list_far_frnds
                      if friend_of_friend != person]
    list_far_frnds.sort()

    return list_far_frnds


def add_score(score_dict: Dict[str, int], scorer: str) -> Dict[str, int]:
    """Add 1 to the scorer's score returning the updated dictionary.

    Docstring examples not given since result depends on input data.
    """
    if scorer in score_dict:
        score_dict[scorer] += 1
    else:
        score_dict[scorer] = 1

    return score_dict


def dict_to_tuple(score_dict: Dict[str, int],
                  person_to_friends: Dict[str, List[str]], person: str)\
        -> List[Tuple[str, int]]:
    """Convert "score_dict" to a list of tuples.

    example: {'Mitchell Pritchett': 4, 'Cameron Tucker': 2,
    'Luke Dunphy': 1, 'Phil Dunphy': 1} converts to [('Mitchell Pritchett', 4),
    ('Cameron Tucker', 2), ('Luke Dunphy', 1), ('Phil Dunphy', 1)]
    """
    final_score_list = []
    for key in score_dict:
        if key not in person_to_friends[person] and key != person:
            tuple_ = tuple([key, score_dict[key]])
            final_score_list.append(tuple_)

    return final_score_list


def mutual_friend_recommendations(person: str,
                                  person_to_friends: Dict[str, List[str]],
                                  potential_friend_dict: Dict[str, int]) \
        -> Dict[str, int]:
    """Add potential friends on the basis of mutual friends in the
    "potential_friend_dict".
    """
    potential_friends = get_friends_of_friends(person_to_friends, person)
    for friend in potential_friends:
        add_score(potential_friend_dict, friend)

    for key in person_to_friends:
        if key not in potential_friend_dict and \
                        person in get_friends_of_friends(person_to_friends, key):
            potential_friend_dict = add_score(potential_friend_dict, key)

    return potential_friend_dict


def network_recommendations(person: str,
                            person_to_networks: Dict[str, List[str]],
                            potential_friend_dict: Dict[str, int]) -> Dict[str, int]:
    """Add potential friends on the basis of network in the
    "potential_friend_dict".
    """
    network_dict = invert_network(person_to_networks)
    for key in network_dict:
        if person in network_dict[key]:
            for fellow_network_member in network_dict[key]:
                potential_friend_dict = add_score(potential_friend_dict,
                                                  fellow_network_member)

    return potential_friend_dict


def family_recommendations(person: str,
                           person_to_friends: Dict[str, List[str]],
                           potential_friend_dict: Dict[str, int]) -> Dict[str, int]:
    """Add potential friends on the basis of last name in the
    "potential_friend_dict".
    """
    family_dict = get_families(person_to_friends)
    for surname in family_dict:
        if family_dict[surname] == person.split(' ')[-1]:
            for fellow_family_member in family_dict:
                if fellow_family_member in potential_friend_dict:
                    potential_friend_dict = add_score(potential_friend_dict,
                                                      fellow_family_member)

    return potential_friend_dict


def sort_dict(dict_: Dict[str, int]) -> Dict[str, int]:
    """Sort dictionary containing potential friends as keys and their score as
    values in decreasing order of their score and in alphabetic order of their
    names for those having same score.

    example:{'Cameron Tucker': 2, 'Luke Dunphy': 1, 'Mitchell Pritchett': 4, '
    Phil Dunphy': 1} returns {'Mitchell Pritchett': 4, 'Cameron Tucker': 2,
    'Luke Dunphy': 1, 'Phil Dunphy': 1}
    """
    alpha_sorted_dict = {}
    keylist = list(dict_.keys())
    keylist.sort()
    for key in keylist:
        alpha_sorted_dict[key] = dict_[key]

    score_sorted_dict = {}
    list_ = [alpha_sorted_dict[key] for key in alpha_sorted_dict]
    list_.sort(reverse=True)
    for score in list_:
        for key in alpha_sorted_dict:
            if score == alpha_sorted_dict[key]:
                score_sorted_dict[key] = score

    return score_sorted_dict


def make_recommendations(person: str,
                         person_to_friends: Dict[str, List[str]],
                         person_to_networks: Dict[str, List[str]])\
        -> List[Tuple[str, int]]:
    """Return a list of tuples, each having name and score of the recommended
     friend.

     Docstring examples not given since result depends on input data.
    """
    potential_friend_dict = {}
    # mutual friends recommendations
    potential_friend_dict = mutual_friend_recommendations(
        person, person_to_friends, potential_friend_dict)
    # network recommendations
    potential_friend_dict = network_recommendations(
        person, person_to_networks, potential_friend_dict)
    # last name recommendations
    potential_friend_dict = family_recommendations(
        person, person_to_friends, potential_friend_dict)

    potential_friend_dict_sorted = sort_dict(potential_friend_dict)

    return dict_to_tuple(potential_friend_dict_sorted, person_to_friends,
                         person)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
