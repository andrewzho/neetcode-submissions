class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        RL = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            L = int(str(s[i:j]))
            i = j + 1
            RL.append(s[i:j+L + 1])
            i = j + L + 1
        return RL

