class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return list()
        num_letter_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        digits_len = len(digits)
        returnlist = num_letter_dict[digits[0]]
        if len(digits)==1:
            return list(returnlist)
        for i in range(len(digits)-1):
            returnlist = self.mutiString(returnlist,num_letter_dict[digits[i+1]])
        return returnlist
    
    def mutiString(self,lettera,letterb):
        result = list()
        for i in range(len(lettera)):
            for j in range(len(letterb)):
                result.append(lettera[i]+letterb[j])
        return result
