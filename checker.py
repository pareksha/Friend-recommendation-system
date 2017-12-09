"""Checker for CSC108 Assignment 3"""

import sys

sys.path.insert(0, './pyta')


print("================= Start: checking coding style =================")

import python_ta
python_ta.check_all('network_functions.py', config='pyta/a3_pyta.txt')

print("================= End: checking coding style =================\n")


print("================= Start: checking parameter and return types =================")

import builtins
import io
import copy
import network_functions as nf # imported here so code that doesn't import correctly gets style checked


# Check for use of functions print and input.
our_print = print
our_input = input

def disable_print(*_args, **_kwargs):
    """ Notices if print is called """
    raise Exception("You must not call built-in function print!")


def disable_input(*_args, **_kwargs):
    """ Notices if input is called """
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input


# sample data for testing
PROF_FILE = io.StringIO('''Pritchett, Mitchell
Chess Club
Pritchett, Gloria''')
SAMPLE_P2F = {'Jay Pritchett': ['Gloria Pritchett'],
              'Gloria Pritchett': ['Manny Delgado', 'Jay Pritchett']}
SAMPLE_P2N = {'Jay Pritchett': ['Parent Teacher Association']}


# Type and simple check nf.load_profiles
p2f = copy.deepcopy(SAMPLE_P2F)
p2n = copy.deepcopy(SAMPLE_P2N)
result = nf.load_profiles(PROF_FILE, p2f, p2n)
assert isinstance(result, type(None)), \
    '''network_functions.load_profiles should return None'''
assert len(p2f) == 3, \
    '''network_functions.load_profiles should add to the person-to-friends dictionary'''
assert len(p2n) == 2, \
    '''network_functions.load_profiles should add to the person-to-networks dictionary'''


# Type and simple check nf.get_families
p2f = copy.deepcopy(SAMPLE_P2F)
result = nf.get_families(p2f)
assert isinstance(result, dict), \
    '''network_functions.get_families should return a dict'''
assert result.get('Pritchett', []) != [], \
    '''network_functions.get_families should return a dictionary where the keys are last names'''
assert isinstance(result.get('Pritchett', ''), list), \
    '''network_functions.get_families should return a dictionary where the values are lists'''
assert isinstance(result.get('Pritchett', '')[0], str), \
    '''network_functions.get_families should return a dictionary where the values are lists of strings'''


# Type and simple check nf.get_average_friend_count
p2f = copy.deepcopy(SAMPLE_P2F)
result = nf.get_average_friend_count(p2f)
assert isinstance(result, float), \
    '''network_functions.get_average_friend_count should return a float'''


# Type and simple check nf.invert_network
p2n = copy.deepcopy(SAMPLE_P2N)
result = nf.invert_network(p2n)
assert isinstance(result, dict), \
    '''network_functions.invert_network should return a dict'''
assert result.get('Parent Teacher Association', []) != [], \
    '''network_functions.invert_network should return a dictionary where the keys are network names'''
assert isinstance(result.get('Parent Teacher Association', ''), list), \
    '''network_functions.invert_network should return a dictionary where the values are lists'''
assert isinstance(result.get('Parent Teacher Association', '')[0], str), \
    '''network_functions.invert_network should return a dictionary where the values are lists of strings'''


# Type and simple check nf.get_friends_of_friends
p2f = copy.deepcopy(SAMPLE_P2F)
result = nf.get_friends_of_friends(p2f, 'Jay Pritchett')
assert isinstance(result, list), \
    '''network_functions.get_friends_of_friends should return a list'''
assert len(result) > 0 and isinstance(result[0], str), \
    '''network_functions.get_friends_of_friends should return a list of strings'''


# Type and simple check nf.make_recommendations
p2f = copy.deepcopy(SAMPLE_P2F)
p2n = copy.deepcopy(SAMPLE_P2N)
result = nf.make_recommendations('Jay Pritchett', p2f, p2n)
assert isinstance(result, list), \
    '''network_functions.make_recommendations should return a list'''
assert len(result) > 0 and isinstance(result[0], tuple), \
    '''network_functions.make_recommendations should return a list of tuples'''
assert len(result[0]) == 2 and isinstance(result[0][0], str) and isinstance(result[0][1], int), \
    '''network_functions.make_recommendations should return a list of (str, int) tuples'''


builtins.print = our_print
builtins.input = our_input

print("================= End: checking parameter and return types =================\n")

print("The parameter and return type checker passed.")
print("This means we will be able to test your code.")
print("It does NOT mean your code is necessarily correct.")
print("You should run your own thorough tests to convince yourself your code is correct.")
print()
print("Review the messages above to see the results of the style checking.")
