import numpy as np
import matplotlib.pyplot as plt


def computeCharEntropy(contents, ranks: int = 4) -> list:
    """
    Computes characters entropy of given rank in provided text file

    :param contents: contents of a text file to be analyzed, as a single string
    :param ranks: highest rank of the entropy to be computed, i.e. on how many other words this one depends on
    """
    # dynamically count all occurrences of grams of size ranks+1 working forwards
    #   i.e. count 1-gram, count 2-gram and so on
    chars_count = [dict() for i in range(ranks + 1)]  # index corresponds to how many previous chars it depends on
    chars_total = 0

    # "-ranks" due to first chars being cut out (not enough prior chars for conditional Entropy)
    for char_idx in reversed(range(len(contents) - ranks)):
        chars_total += 1
        gram = ""
        count_idx = 0
        for shift in reversed(range(ranks + 1)):  # add every character to finally form ranks-gram
            gram += contents[char_idx - shift]
            if gram in chars_count[count_idx]:
                chars_count[count_idx][gram] += 1
            else:
                chars_count[count_idx][gram] = 1
            count_idx += 1

    # calculate the entropy
    entropy = [0.0 for i in range(ranks + 1)]

    # "based-on-0" is unique, as it doesn't depend on any previous chars
    for item in chars_count[0]:
        entropy[0] += chars_count[0][item] / chars_total * np.log2(chars_total / chars_count[0][item])  # inverted prob

    # i is the rank index
    for i in range(1, ranks + 1):
        for item in chars_count[i]:
            prev_key = item[:-1]
            entropy[i] += chars_count[i][item] / chars_total * np.log2(
                chars_count[i - 1][prev_key] / chars_count[i][item])

    print(entropy)
    return entropy


def computeWordEntropy(separated_contents, ranks: int = 4) -> list:
    """
    Computes words entropy of given rank in provided text file

    :param separated_contents: separated contents of a text file to be analyzed, as a list
    :param ranks: highest rank of the entropy to be computed, i.e. on how many other words this one depends on
    """
    # dynamically count all occurrences of word combinations of size ranks+1 working forwards
    #   i.e. count word1-, count word1-word2 and so on
    words_count = [dict() for i in range(ranks + 1)]  # index corresponds to how many previous words it depends on
    words_total = 0

    # "-ranks" due to first words being cut out (not enough prior words for conditional Entropy)
    for word_idx in reversed(range(len(separated_contents) - ranks)):
        words_total += 1
        comb = ""
        count_idx = 0
        for shift in reversed(range(ranks + 1)):  # add every character to finally form ranks-gram
            comb += separated_contents[word_idx - shift] + "-"
            if comb in words_count[count_idx]:
                words_count[count_idx][comb] += 1
            else:
                words_count[count_idx][comb] = 1
            count_idx += 1

    # calculate the entropy
    entropy = [0.0 for i in range(ranks + 1)]

    # "based-on-0" is unique, as it doesn't depend on any previous words
    for item in words_count[0]:
        entropy[0] += words_count[0][item] / words_total * np.log2(words_total / words_count[0][item])  # inverted prob

    # i is the rank index
    for i in range(1, ranks + 1):
        for item in words_count[i]:
            # remove the last word
            item_split = item.split("-")
            prev_key = ""
            for j in range(len(item_split) - 2):
                prev_key += item_split[j] + "-"

            entropy[i] += words_count[i][item] / words_total * np.log2(
                words_count[i - 1][prev_key] / words_count[i][item])

    print(entropy)
    return entropy


def computeEntropies(filepaths, png_name, do_char: bool = True, do_word: bool = True, ranks: int = 4):
    """
    Computes specified entropy (char and/or word) for ranks starting from 0 up to the specified number.
    Exports the plot of Entropy change with respect to the rank change.

    :param filepaths: list of paths to the text files to be analyzed
    :param do_char: specifies if char entropy should be computed
    :param do_word: specifies if word entropy should be computed
    :param ranks: number of ranks; i.e. up to how many chars/words a conditional entropy should go on
    """
    if not do_char and not do_word:
        print("No char and no word entropy wanted -> no output")
        return

    print("running computations for \"{}\"".format(png_name))
    x = [i for i in range(ranks + 1)]
    if do_char:
        print("(computing char entropy)")
        for filepath in filepaths:
            print("\tcurrent file: {}".format(filepath))
            with open(filepath, 'r') as file:
                contents = file.readline()  # as everything's in one row
            label_text = filepath.split("/")
            label_text = label_text[len(label_text) - 1].split(".")[0]
            plt.plot(x, computeCharEntropy(contents, ranks), label=label_text)
        plt.legend()
        plt.title("Con.Ent./Con.Ent.Order - Char")
        plt.xlabel("conditional entropy order")
        plt.ylabel("conditional entropy value")
        plt.savefig(png_name + "-char.png")
        plt.close()
        print("done\n")

    if do_word:
        print("(computing word entropy)")
        for filepath in filepaths:
            print("\tcurrent file: {}".format(filepath))
            with open(filepath, 'r') as file:
                contents = file.readline().split()
            label_text = filepath.split("/")
            label_text = label_text[len(label_text) - 1].split(".")[0]
            plt.plot(x, computeWordEntropy(contents, ranks), label=label_text)
        plt.legend()
        plt.title("Con.Ent./Con.Ent.Order - Word")
        plt.xlabel("conditional entropy order")
        plt.ylabel("conditional entropy value")
        plt.savefig(png_name + "-word.png")
        plt.close()
        print("done\n")


# main program
norm_filepaths = ["text-files/norm_wiki_en.txt", "text-files/norm_wiki_eo.txt", "text-files/norm_wiki_et.txt",
                  "text-files/norm_wiki_ht.txt", "text-files/norm_wiki_la.txt", "text-files/norm_wiki_nv.txt",
                  "text-files/norm_wiki_so.txt"]
computeEntropies(norm_filepaths, "norm", do_char=True, do_word=True, ranks=5)
sample_filepaths = ["text-files/sample0.txt", "text-files/sample1.txt", "text-files/sample2.txt",
                    "text-files/sample3.txt", "text-files/sample4.txt", "text-files/sample5.txt"]
computeEntropies(sample_filepaths, "sample", do_char=True, do_word=True, ranks=5)
