class Solution:
    def sortVowels(self, s: str) -> str:
        # vowel = ['a','e','i','o','u','A','E','I','O','U']
        # t = []
        # pos = []
        # for i in range(len(s)):
        #     if s[i] in vowel:
        #         t.append("-1")
        #         pos.append(s[i])
        #     else:
        #         t.append(s[i])
        # # print(f't {t} and pos {pos}')
        # pos.sort()
        # # print(f't {t} and pos {pos}')
        # for i in range(len(t)):
        #     if t[i] == "-1":
        #         t[i] = pos.pop(0)
        # t = "".join(t)
        # return t
        vowel = []
        pos = []
        for i,c in enumerate(s):
            if c.lower() in ['a','e','i','o','u']:
                vowel.append(c)
                pos.append(i)
        vowel.sort()
        s = list(s)
        for i,v in zip(pos,vowel):
            s[i] = v
        
        return "".join(s)