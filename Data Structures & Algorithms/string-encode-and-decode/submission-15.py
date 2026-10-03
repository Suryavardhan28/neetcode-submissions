class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + (str(len(s))) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        res_string = s
        while(len(res_string)>0):
            hash_index = res_string.find('#')
            str_length = int(res_string[:hash_index])
            res.append(res_string[hash_index+1:hash_index+1+str_length])
            res_string = res_string[hash_index+1+str_length:]
        return res