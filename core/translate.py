from .utils import parse_term


# find direct translation from english word
def get(data: dict,term: str) -> str or None:
    parsed_term = parse_term(term)
    
    result = data.get(parsed_term)
    try:
        return result[0]
    except TypeError:
        return None
    
def find(data: dict, term: str) -> list or None:
    parsed_term = parse_term(term)
    
    result = data.get(parsed_term)
    try:
        return result
    except TypeError:
        return None

def propose(data : dict,term: str) -> dict:
    """_summary_

    Args:
        data (dict): Dict with translations of shape: {term_in: [result1,result2],...}
        term (str): Term looking for
        acc (int): Accuracy of match of the proposition

    Returns:
        list:
    """
    parsed_term = parse_term(term)
    
    propositions = {}
    
    for key,results in data.items():
        if key.find(parsed_term) == 0:
            propositions[key] = results
    return propositions
    
    