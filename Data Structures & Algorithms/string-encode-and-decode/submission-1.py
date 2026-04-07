class Solution:

    def encode(self, strs: List[str]) -> str:
        toRet = ""
        for s in strs:
            toRet += str(len(s)) + "#" + s
        print(toRet)
        return toRet

    def decode(self, s: str) -> List[str]:
        strList = []
        index = 0
        lengthOfNextString = ""
        while index < len(s):
            if s[index] != "#":
                lengthOfNextString += s[index]
                index += 1
                print(lengthOfNextString)
            else:
                word = s[index + 1: index + 1 + int(lengthOfNextString)]
                print(word)
                strList.append(word)
                index += int(lengthOfNextString) + 1
                lengthOfNextString = ""
        return strList

