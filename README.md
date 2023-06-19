# CatGPT-Autocomplete

## Background

AI has been very popular these days, we humans benefits from AI in many different asppects of our life, from using as a chatbot to predicting the next word that we would use, aka auto-complete. However, cats deserves to use some of these AI too !!!

Some cat expert named Kattie, claims that there are 26 words in the cat's vocabulary and each words can be mapped to the 26 letters of the English language. For instance,

- meow = a
- meoow = b
- meuw = c
- meuuw = d
- meuow = e
- . . .
- nyan = y
- meowth = z

As a cat lover, Kattie has collected a large data set of cat sentences that are used by cats all around the world. For example, The cat sentence "meow meoow meowth" can then be represented as "abz".

Given the large datasets of cat sentences, an auto-complete feature can be then produced based on the cat senetence that are most frequently used among the cats. Cats can now enjoy the benefit of "AI" which is just a text prediction model produced using a Trie data structure.

## Approach Description

Given the list of cat sentences, construct a Trie data structure by inserting each and every character into the Trie. During the insertion process keeps track of the frequency of the cat sentences inserted. Given the word to auto-complete, a simple traversal down the breadcrumbs left during the insertion process would return the auto-completed cat sentence

## Example

Given a list of cat sentences:

sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz", "abazacy", "dbcef", "xyz", "xxx", "xzz"]

Given a prompt "ab", the auto-complete feauture would return "abazacy" as this cat sentences that are most frequently used with a prefix of "ab" is "abazacy"

## Instructions

1. Download the "auto-complete.py" python file
2. Run the file given the inputs
3. Feel free to modify the inputs as you wish

## Contributing

1. Chan Yanhan
2. Monash School of IT FIT1008 & FIT2004 Teaching Team
