class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if not words:
            return False

        freq = [0] * 26

        for word in words:
            for char in word:
                freq[ord(char) - ord("a")] += 1

        return all(count % len(words) == 0 for count in freq)