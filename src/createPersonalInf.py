import random
from datetime import datetime


# List of profiles
profiles = [
    "Name: Ahmed, Gender: Male, Age: 21",
    "Name: Nour, Gender: Female, Age: 18",
    "Name: Omar, Gender: Male, Age: 45",
    "Name: Salma, Gender: Female, Age: 27",
    "Name: Ali, Gender: Male, Age: 62",
    "Name: Assma, Gender: Female, Age: 24",
    "Name: Karim, Gender: Male, Age: 18",
    "Name: Mona, Gender: Female, Age: 21",
    "Name: Youssef, Gender: Male, Age: 24",
    "Name: Mariam, Gender: Female, Age: 62",
    "Name: Ali, Gender: Male, Age: 27",
    "Name: Fatima, Gender: Female, Age: 45",
]

def get_random_profile():
    # Get the current seconds
    current_time = datetime.now()
    seconds = current_time.second
    
    # Use the seconds to determine the index (modulo the number of profiles)
    index = seconds % len(profiles)
    
    return profiles[index]




