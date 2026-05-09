class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "/" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            slash = s.index("/", i)
            length = int(s[i:slash])
            strs.append(s[slash + 1 : slash + 1 + length])
            i = slash + 1 + length

        return strs
