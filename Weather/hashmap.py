class  hashmap:
    def __init__(self):
        self.size=10
        self.hash=[None]*self.size
    def indexr(self,key):
        return hash(key)%self.size
    def add(self,key,value):
        idx=self.indexr(key)
        if self.hash[idx] is None:
            self.hash[idx]=[[key,value]]
        else:
            sublist=self.hash[idx]
            for pair in sublist:
                if pair[0]==key:
                    pair[1]= value
                    return
            self.hash[idx].append([key,value])
    def get(self,key):
        idx=self.indexr(key)
        if self.hash is not None:
            sublist=self.hash[idx]
            for pair in sublist:
                if pair[0]==key:
                    print(pair[1])
    def __delitem__(self, key):
        idx=self.indexr(key)
        if self.hash[idx]:
            sublist=self.hash[idx]
            for i,pair in enumerate(sublist):
                if pair[0]==key:
                    del self.hash[idx][i]






d=hashmap()
d.add("santhosh",3)
d.add("ram",45)
d.add("ram",67)
d.add("rote",45)
d.add("rytu",45)
print(d.hash)
del d["rote"]
print(d.hash)




