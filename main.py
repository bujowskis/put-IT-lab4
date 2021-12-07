

def computeCharEntropy(filepath, rank: int = 0):
    """
    Computes characters entropy of given rank in provided text file

    :param filepath: path to the text file to be analyzed
    :param rank: rank of the entropy, i.e. on how many other characters this one depends
    """
    count = dict()  # counts of occurrence of all different rank-grams
    with open(filepath, 'r') as file:
        contents = file.readline()  # as everything is in one row

        # "- rank" due to first chars being cut out (not enough prior chars)
        for char_idx in reversed(range(len(contents) - rank)):
            rank_gram = ""
            for shift in reversed(range(rank+1)):
                rank_gram += contents[char_idx - shift]
            if rank_gram in count:
                count[rank_gram] = count[rank_gram] + 1
            else:
                count[rank_gram] = 1
    print(count)


def computeWordEntropy(filepath, rank: int = 0):
    """
    Computes words entropy of given rank in provided text file

    :param filepath: path to the text file to be analyzed
    :param rank: rank of the entropy, i.e. on how many other words this one depends
    """
    ...


# main program TODO - make a "centralization function" reading the text file only once
computeCharEntropy("text-files/norm_wiki_en.txt", 0)
computeCharEntropy("text-files/norm_wiki_en.txt", 1)
computeCharEntropy("text-files/norm_wiki_en.txt", 2)