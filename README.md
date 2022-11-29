# put-IT-lab4
Detecting natural languages using conditional entropy analysis - Repository for PUT's Information Theory lab4 assignment

## Simple, approachable description
If we received a signal - a "message" - from outer space, how would we know it is, in fact, a message in some alien language? One of the best methods we could use is `conditional entropy analysis`.

For virtually all natural languages (not only in humans but also in animal communication), some words/characters occur more often after one another. For example:
- after the words "do you", the next word is likely going to be "like" (as in "do you like"), while it's unlikely to be "you" (as in "do you you")
- after the characters "do you like it", the next character is likely going to be "?" (as in "do you like it?"), while it's unlikely to be "z" (as in "do you like itx")

This likelihood produces a common pattern seen in virtually all natural languages - animal, human, from the past, modern ones - you name it.

The main takeaway is - ***natural languages are quite predictable*** - the more previous words/characters we take into account, the more predictable the next ones are.

`Entropy` put simply, is a measure of chaos and uncertainty. When entropy equals 0, something is fully predictable. The bigger the entropy, the more chaotic and unpredictable something is.

`Conditional entropy` is used to determine if (and by how much) something becomes less chaotic (i.e. more predictable) when taking into account some factors.

Subtract Entropy from Conditional Entropy and you get `Information Gain` - the measure of how much information taking into account a given factor brings you.

Coming back to the problem - we can apply conditional entropy analysis to the received message and check if the pattern common in natural languages occurs (natural language? aliens?) or not.

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

### Char graph
Undoubtedly, the most repulsive option here is the sample4. It's not as stretched and curves exactly the other way we
want in a natural language.

The next one is sample0, which seems to be too curved and has almost no change from order 3
to 5.

I'm also unsure about sample5, as it doesn't drop that much over order 1 to 3, compared to order 0 to 1, forming a
"bump", but such a bump (though smaller) can be observed for norm_wiki-et.

###Summing up the Char plot:

- **potential good candidates** - `sample1`, `sample3`
- **still a chance** - `sample2`, `sample5`
- **opposition** - `sample0`, `sample4`

### Word graph
At the first glance, we can remove `sample5` from the candidates for natural languages. Instead of a gradual decrease in
conditional entropy, it drops to 0 after taking into account just a single prior word. I suppose what happens here is,
the words are so much random, such that just taking into account one prior word makes all the conditional entropy 0, as
there's only one word for every one prior word to occur after it - i.e., there is only a single word that occurs after a
any word in this text sample.

The next "weirdos" of the plot are `sample0` and `sample2`. Instead of a gradually slowing decrease, their entropy drops
only slightly over 0-1 and 3-5, while over 1-3 it's relatively much steeper.

Also, `sample4` is the only to drop almost as steep as radical `sample5`, but it keeps the exponential decay patter.
It's just much "violent" and faster-convergent than the other samples.

###Summing up the Word plot:

- **potential good candidates** - `sample1`, `sample3`
- **unusual, but interesting** - `sample4`
- **rejected** - `sample0`, `sample2`, `sample5`

### Char and Word combined - the final decisions

- `sample0` - not a natural language (Word test)
- `sample1` - natural language (both tests passed)
- `sample2` - not a natural language (Word test)
- `sample3` - natural language (both tests passed)
- `sample4` - still unsure; **see dilemma below**
- `sample5` - not a natural language (Word test)

### The interesting case of `sample4`

Even though at first I was going to reject this sample based on completely different behavior during Char test and a
suspicious result of Word test, the more I thought about it, the more in doubt I was. On one hand, it seems to be
very "messy". Compared to the languages we're used to, it may seem simply random. It contains words of very varying
lengths - it's possible to find a "word" consisting of a single character, as well as a *really* long "noodle" such as

`gaamd2oaoiiotobahontscadsrnetlsiplatueaptet`

On the other hand, even though its entropy dropped and converged really fast, it's not as in case of `sample5`, which
is without any doubt random. Compare the entropy values of Word test we get for:

`sample5`:
```
current file: text-files/sample5.txt
[16.50952745314629, 0.0, 0.0, 0.0, 0.0, 0.0]
```

and `sample4`:
```
current file: text-files/sample4.txt
[17.129660116882004, 3.44426436014238, 0.23407639869387514, 0.003227431119931433, 7.60889828044334e-06, 0.0]

```

The tiny differences in order 2, 3 and 4 between these two are fascinating. Why? In case of `sample5`, the entropy
became 0 right away, whereas in `sample4` it was still positive all the way up to order 5.

On top of that, the initial order 0 entropy of `sample4` is higher compared to other natural-language samples and norms,
which indicates a greater variety and frequency of words.

Honestly, in my opinion it may mean two things - either `sample4` is in fact random, with repeating words consisting of
just a few characters making up the marginal remaining entropy, OR it **is** a natural language, which cannot be
represented well using the available characters (think of hanzi - logograms developed for writing Chinese), containing
lots of meaning in just a few words.

Representing all (possibly huge) amount of logograms using the available characters
would lead to creation of (possibly long and repulsing and seemingly gibberish or random) words, making the Char test
inapplicable.

On the other hand, using just a few logograms (words) could make up a whole sentence, which using a language such as
English would require 10 and more words.

The **final point** regards `sample4` is - I'd say it *may be* a natural language, in the form I described above.
I'm almost sure excluding it would be a safer option, but the idea is so interesting I'm willing to take the risk. I
hope for a good talk regards that.
