

def computeCharEntropy(contents, ranks: int = 4) -> list:
    """
    Computes characters entropy of given rank in provided text file

    :param contents: contents of a text file to be analyzed, as a single string
    :param ranks: highest rank of the entropy to be computed, i.e. on how many other words this one depends
    """
    chars_count = [dict() for i in range(ranks+1)]  # list index corresponds to how many prior chars depends on
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

    print("(chars)")
    for di in chars_count:
        print(di)
        print("\n")

    return []  # todo - return list of entropy


def computeWordEntropy(separated_contents, ranks: int = 4) -> list:
    """
    Computes words entropy of given rank in provided text file

    :param separated_contents: separated contents of a text file to be analyzed, as a list
    :param ranks: highest rank of the entropy to be computed, i.e. on how many other words this one depends
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
computeEntropies("text-files/norm_wiki_en.txt", do_char=True, do_word=False, ranks=2)