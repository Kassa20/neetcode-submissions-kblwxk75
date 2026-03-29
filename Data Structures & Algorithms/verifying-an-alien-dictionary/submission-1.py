class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = defaultdict(int)
        for i, c in enumerate(order):
            d[c] = i 

        for i in range(len(words) - 1):
            word = words[i]
            word2 = words[i+1]
            same = 0
            for j in range(len(min(word, word2))):
                if d[word[j]] > d[word2[j]]:
                    return False
                elif d[word[j]] == d[word2[j]]:
                    same += 1
                    continue
                else:
                    break

            if same == len(word2) and len(word) > len(word2):
                return False


        return True