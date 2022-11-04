from fuzzywuzzy import fuzz, process

def keyword_search(key: str, choices: list,):
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
    matches = process.extract(query=key, choices=choices, limit=5)
    
    print()
    print(f'You searched for: {key}')
    print()
    print('(Book title, confidence score, list index)')
    print("\n".join(map(str, matches)))
    print()
    print(f'Closest match {matches[0]}')
    print()
    
    return(matches[0])