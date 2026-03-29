class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls= 0
        cows = 0
        count = {}
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                count[s] = count.get(s, 0) + 1
        for s, g in zip(secret, guess):
            if s != g and count.get(g, 0) > 0:
                cows += 1
                count[g] -= 1

        return f"{bulls}A{cows}B"