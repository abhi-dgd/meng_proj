# Import Python libraries
import time


# Import installed libraries
from fuzzywuzzy import fuzz, process


def keyword_search(key: str, choices: list):
    """
    Function to provide input to the recommender functionn. Prints relevant
    information about the keyword searched, the closest matching title,
    confidence on the match, and the index of the book.

    Parameters
    ----------
    key:    str
            User input. Any word or complete title from titles of books which
            exist in the list available
        
    choices: list or Pandas DataFrame
             List from which the algorithm will compare and provide the closest
             match to keyword search

    Returns
    ----------
    matches: tuple
             Tuple of what the algorithm thinks is the closest match to the 
             keyword searched

    """
    matches = process.extract(query=key, choices=choices, limit=3)
    
    #print("\n".join(map(str, matches)))
    print(f'Book you searched: {key}')
    print()
    confirm_user_ip = input('Proceed ([y]/n)?: ')
    print()
    if (confirm_user_ip == 'y'):
        print('FuzzyWuzzy confidence output:')
        print('Book title, confidence score, list index')
        for match in matches:
            print(match)
        print()
        print(f'Recommendations being generated for: {matches[0][0]}')
        print()
        return(matches)
    elif (confirm_user_ip == 'n'):
        new_search = input('Search changed to: ')
        matches_again = process.extract(query=new_search, choices=choices, limit=3)
        print('FuzzyWuzzy confidence output:')
        print('Book title, confidence score, list index')
        print(f'Book you are now searching: {new_search}')
        for match in matches_again:
            print(match)
        print()
        print(f'Recommendations being generated for: {matches_again[0][0]}')
        print()
        return(matches_again)


def fake_wait(wait_for: int,):
    print('Generating recommendations...', end='', flush=True)
        
    for x in range(wait_for):
            for frame in r'-\|/-\|/':
                # Back up one character then print our next frame in the animation
                print('\b', frame, sep='', end='', flush=True)
                time.sleep(0.2)

        # Back up one character, print a space to erase the spinner, then a newline
        # so that the prompt after the program exits isn't on the same line as our
        # message
        
    print('\b ')
    print()