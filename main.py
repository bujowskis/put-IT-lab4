

def computeCharEntropy(contents, rank: int = 0) -> float:
    """
    Computes characters entropy of given rank in provided text file

    :param contents: contents of a text file to be analyzed, as a single string
    :param rank: rank of the entropy, i.e. on how many other characters this one depends
    """
    count = dict()  # counts of occurrence of all different rank-grams in the text

    # "- rank" due to first chars being cut out (not enough prior chars)
    # todo - exclude spaces and numbers?
    for char_idx in reversed(range(len(contents) - rank)):
        n_gram = ""
        for shift in reversed(range(rank+1)):
            n_gram += contents[char_idx - shift]
        if n_gram in count:
            count[n_gram] = count[n_gram] + 1
        else:
            count[n_gram] = 1
    print(count)

    return 0.0  # todo


def computeWordEntropy(separated_contents, rank: int = 0) -> float:
    """
    Computes words entropy of given rank in provided text file

    :param separated_contents: separated contents of a text file to be analyzed, as a list
    :param rank: rank of the entropy, i.e. on how many other words this one depends
    """
    count = dict()  # counts of occurrence of all different words combinations of length rank+1 in the text

    # "- rank" due to first chars being cut out (not enough prior chars)
    for word_idx in reversed(range(len(separated_contents) - rank)):
        comb = ""
        for shift in reversed(range(rank+1)):
            comb += separated_contents[word_idx - shift]
            comb += "-"
        if comb in count:
            count[comb] = count[comb] + 1
        else:
            count[comb] = 1
    print(count)

    return 0.0  # todo


def computeEntropies(filepath, do_char: bool = True, do_word: bool = True, ranks=None):
    if ranks is None:
        ranks = [0, 1, 2, 3, 4]  # todo - adjust values
    ranks_no = len(ranks)
    with open(filepath, 'r') as file:
        contents = file.readline()  # as everything's in one row

    if do_char:
        char_entropy = [0.0 for i in range(ranks_no)]
        for i in range(ranks_no):
            char_entropy[i] = computeCharEntropy(contents, ranks[i])
        # todo - consider using matplotlib to show/export a graph

    if do_word:
        separated_contents = contents.split()
        word_entropy = [0.0 for i in range(ranks_no)]
        for i in range(ranks_no):
            word_entropy[i] = computeWordEntropy(separated_contents, ranks[i])
        # todo - consider using matplotlib to show/export a graph


# main program
computeEntropies("text-files/norm_wiki_en.txt", do_char=True, do_word=True, ranks=[0, 1, 2])