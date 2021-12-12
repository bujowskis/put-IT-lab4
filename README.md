# put-IT-lab4
Repository for PUT's Information Theory lab4 assignment - Conditional entropy of natural languages

## General description
For "behind the scenes", please see `lab4-description.pdf`. Basically, the idea is, it's true that for natural
languages, due to some characters and/or words occurring more often one after another, as we take more and more prior
characters/words into account, the total conditional entropy drops. Moreover, the drop follows a pattern which can be
seen in `norm-char.png` and `norm-word.png`.

The task is to evaluate if provided sample texts potentially contain a natural language, or are just more or less
random. It can be done by doing this conditional entropy test and comparing the similarity of sample results obtained
from texts known to be natural languages.

## Deduced answers

Based on the patterns seen from results obtained from natural languages norms, it can be seen that:

- conditional entropy for **Char** should be (more or less) a horizontally stretched exponential decay
- conditional entropy for **Word** should be a nicer looking exponential decay

Moreover, as can be seen from **Word** conditional entropy, the **amount of initial entropy doesn't seem to be a
relevant factor**. I'm convinced that's partially due to some languages having more specific words describing just the
specific things, while some having less words with many meanings (e.g. approx. over 1,000,000 words in Korean vs "just"
about 500,000 in English). Because of this, I believe **the most important factor is the right pattern**, and that's how
I'm going to approach the evaluation.

Also, **Word** conditional entropy seems to be a better indication than char, since all languages seem to converge more
similarly than in case of **Char** entropy. That's because by looking at words, we get **more context** than in case of
just characters, which in turn gives us even more information with every next word taken into account for the
conditional entropy. That's why I'm going to use it as a more powerful factor in evaluation process. That means, there's
a bigger tolerance for deviations in **Char** entropy than in case of **Word** entropy.

For simplicity, I'm going to use the following references as a convention:

- graph of character conditional entropy = **Char graph**
- graph of words conditional entropy = **Word graph**

## Char graph
Undoubtedly, the most repulsive option here is the sample4. It's not as stretched and curves exactly the other way we
want in a natural language. The next one is sample0, which seems to be 