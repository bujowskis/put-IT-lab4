

def computeCharEntropy(filepath, rank: int = 0):
    """
    Computes characters entropy of given rank in provided text file

    :param filepath: path to the text file to be analyzed
    :param rank: rank of the entropy, i.e. on how many other characters this one depends
    """
    enmat = list()  # entropy matrix
    with open(filepath, 'r') as file:
        ...


def computeWordEntropy(filepath, rank: int = 0):
    """
    Computes words entropy of given rank in provided text file

    :param filepath: path to the text file to be analyzed
    :param rank: rank of the entropy, i.e. on how many other words this one depends
    """
    ...

