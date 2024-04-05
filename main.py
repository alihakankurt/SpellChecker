from spellchecker import SpellChecker

if __name__ == "__main__":
    checker: SpellChecker = SpellChecker()
    checker.add_words(["apple", "people"])
    result: list[(str, int)] = checker.check("ppl")
    print(result)
