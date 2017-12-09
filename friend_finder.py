""" CSC108 Assignment 3: Friend Finder - Main Program code """
from typing import List
from network_functions import load_profiles, make_recommendations

   
def display_recommendations(potential_friends: List[str]) -> None:
    """Display the recommendations in potential_friends or a message
    indicating that there are no recommendations.
    """

    if len(potential_friends) > 0:
        for name in potential_friends:
            print(name)
    else:
        print("There are no recommendations for this person.")       


if __name__ == '__main__':
    friendships = {}
    networks = {}
    profiles_file = open('profiles.txt')
    load_profiles(profiles_file, friendships, networks)
    
    person = input('Please enter a person (or press return to exit): ')    
    while person != '':
        potential = make_recommendations(person, friendships, networks)
        display_recommendations(potential)
        person = input('\nPlease enter a person (or press return to exit): ') 
    print("Thank you for using the recommendation system!")
