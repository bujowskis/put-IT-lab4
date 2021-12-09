import numpy as np

def computeCharEntropy(contents, ranks: int = 4) -> list:
    """
    Computes characters entropy of given rank in provided text file

    :param contents: contents of a text file to be analyzed, as a single string
    :param ranks: highest rank of the entropy to be computed, i.e. on how many other words this one depends on
    """
    # dynamically count all occurrences of grams of size ranks+1 working forwards
    #   i.e. count 1-gram, count 2-gram and so on
    chars_count = [dict() for i in range(ranks+1)]  # index corresponds to how many previous chars it depends on
    chars_total = 0

    # "-ranks" due to first chars being cut out (not enough prior chars for conditional Entropy)
    for char_idx in reversed(range(len(contents) - ranks)):
        chars_total += 1
        gram = ""
        count_idx = 0
        for shift in reversed(range(ranks+1)):  # add every character to finally form ranks-gram
            gram += contents[char_idx - shift]
            if gram in chars_count[count_idx]:
                chars_count[count_idx][gram] += 1
            else:
                chars_count[count_idx][gram] = 1
            count_idx += 1

    # calculate the entropy
    entropy = [0.0 for i in range(ranks+1)]

    # "based-on-0" is unique, as it doesn't depend on any previous chars
    for item in chars_count[0]:
        entropy[0] += chars_count[0][item]/chars_total * np.log2(chars_total/chars_count[0][item])  # inverted prob

    # i is the rank index
    for i in range(1, ranks+1):
        prev_key = None
        for item in chars_count[i]:
            if not prev_key:
                prev_key = item[:-1]  # get the key to the "one rank above" count
            entropy[i] += chars_count[i][item]/chars_total * np.log2(chars_count[i-1][prev_key]/chars_count[i][item])

    print(entropy)

    return entropy  # todo - return list of entropy / export plot from here


def computeWordEntropy(separated_contents, ranks: int = 4) -> list:
    """
    Computes words entropy of given rank in provided text file

    :param separated_contents: separated contents of a text file to be analyzed, as a list
    :param ranks: highest rank of the entropy to be computed, i.e. on how many other words this one depends on
    """
    count = dict()  # counts of occurrence of all different words combinations of length rank+1 in the text
    count1 = dict()  # same as above, but excluding the last word - i.e. count of all word combinations of size rank

    # "- rank" due to first chars being cut out (not enough prior words for conditional entropy)
    for word_idx in reversed(range(len(separated_contents) - rank)):
        comb1 = ""
        for shift in reversed(range(1, rank+1)):
            comb1 += separated_contents[word_idx - shift]
            comb1 += "-"
        comb = comb1 + separated_contents[word_idx]
        if comb in count:
            count[comb] = count[comb] + 1
        else:
            count[comb] = 1
        if comb1 in count1:
            count1[comb1] += 1
        else:
            count1[comb1] = 1
    print("words")
    for item in count1:
        print("count1 of \"{}\": {}".format(item, count1[item]))
        break
    for item in count:
        print("count of \"{}\": {}".format(item, count[item]))
        break

    return []  # todo - return list of entropy


def computeEntropies(filepath, do_char: bool = True, do_word: bool = True, ranks: int = 4):
    """
    Computes specified entropy (char and/or word) for ranks starting from 0 up to the specified number.
    Exports the plot of Entropy change with respect to the rank change.

    :param filepath: path to the text file to be analyzed
    :param do_char: specifies if char entropy should be computed
    :param do_word: specifies if word entropy should be computed
    :param ranks: number of ranks; i.e. up to how many chars/words a conditional entropy should go on
    """
    if not do_char and not do_word:
        print("No char and no word entropy wanted -> no output")
        return

    # todo - create and export graphs (probably from within functions below)
    with open(filepath, 'r') as file:
        contents = file.readline()  # as everything's in one row

    if do_char:
        char_entropy = computeCharEntropy(contents, ranks)

    if do_word:
        separated_contents = contents.split()
        word_entropy = computeWordEntropy(separated_contents, ranks)


# main program
computeEntropies("text-files/norm_wiki_en.txt", do_char=True, do_word=False, ranks=4)