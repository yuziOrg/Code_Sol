class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l1=len(s)
        l2=len(t)
        smap={}
        tmap={}
        left=0
        right=0
        min_len=math.inf
        min_string=""
        if(l2>l1):
            return ""
        for i in range(l2):
            smap[s[i]]=smap.get(s[i],0)+1
            tmap[t[i]]=tmap.get(t[i],0)+1
        if(tmap==smap):
            return s[0:l2]
            
            
        #print(smap,tmap)
        for right in range(l2,l1):
            smap[s[right]]=smap.get(s[right],0)+1
            #print(right,smap)
            while(valid_window(smap,tmap)):
                #print("inside")
                if(right-left+1 < min_len):
                    min_string=s[left:right+1]
                   # print(" .... ",min_string)
                    min_len=right-left+1
                smap[s[left]]-=1
                if(smap[s[left]] == 0):
                    del smap[s[left]]
                left+=1
        return min_string

def valid_window(smap,tmap):
    for key in tmap:
        if(tmap[key] <= smap.get(key,0)):
            pass
        else:
            return False
    return True
