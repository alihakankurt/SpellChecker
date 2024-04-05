# Spell Checker

## Description

A spell checker that searchs for the similar words and returns the found words with their respective edit distance. It uses [Wagner-Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm) to find edit distance between two word.

## Example Usage

```python
# Create an instance of spell checker
checker = SpellChecker()

# Add words to it
checker.add_words(["apple", "people"])

# Search for similar words with maximum edit distance of 2
result = checker.check("ppl")

print(result) # [('apple', 0)]
```
