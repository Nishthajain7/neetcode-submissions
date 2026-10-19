class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words={}
        out=[]
        for str in strs:
            count=[0]*26
            for char in str:
                count[ord(char)-ord('a')]+=1
            count=tuple(count)
            if count in words:
                words[count].append(str)  
            else:
                words[count] = [str]
        for word in words:
            out.append(words[word])
        return out





        