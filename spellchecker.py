class SpellChecker:
    def __init__(self) -> None:
        self.words: list[str] = []

    def add_words(self, words: list[str]):
        self.words.extend(words)

    def add_words_from_file(self, filepath: str, seperator: str = ",") -> None:
        with open(filepath, "r") as file:
            content: str = file.read()

        words: list[str] = map(lambda word: word.strip(), content.split(seperator))
        self.add_words(words)

    def check(self, word: str, limit: int = 10, distance: int = 2) -> list[(str, int)]:
        result: list[(str, int)] = []
        wordLength: int = len(word)

        for target in self.words:
            targetLength: int = len(target)

            currentRow: list[int] = [y for y in range(targetLength + 1)]
            for y in range(1, wordLength + 1):
                previousRow: list[int] = currentRow
                currentRow = [y] + [0 for _ in range(targetLength)]
                for x in range(1, targetLength + 1):
                    addition: int = previousRow[x] + 1
                    deletion: int = currentRow[x - 1] + 1
                    substitution: int = previousRow[x - 1] + (word[y - 1] != target[x - 1])
                    currentRow[x] = min(addition, deletion, substitution)

            targetDistance: int = currentRow[targetLength]
            if targetDistance <= distance:
                result.append((target, targetDistance))

        return sorted(result, key=lambda x: x[1])[:limit]
