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

            dp: list[list[int]] = [
                [x if y == 0 else y if x == 0 else 0
                    for x in range(targetLength + 1)]
                for y in range(wordLength + 1)
            ]

            for y in range(wordLength):
                for x in range(targetLength):
                    dp[y + 1][x + 1] = min(dp[y][x], dp[y][x + 1], dp[y + 1][x]) + (word[y] != target[x])

            targetDistance: int = dp[wordLength][targetLength]
            if targetDistance <= distance:
                result.append((target, targetDistance))

        return sorted(result, key=lambda x: x[1])[:limit]
