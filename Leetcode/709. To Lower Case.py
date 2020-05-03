class Solution:
    def toLowerCase(self, str: str) -> str:
        l = []
        constDif = ord('a') - ord('A')
        lowS = ord('a')
        lowF = ord('z')
        upS = ord('A')
        upF = ord('Z')
        for s in str:
            codeS = ord(s)
            if codeS >= lowS and codeS <= lowF:
                l.append(s)
            elif codeS >= upS and codeS <= upF:
                l.append(chr(codeS+constDif))
            else:
                l.append(s)
        return ''.join(l)