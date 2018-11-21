d = {'f':4, 'a':9, 'e':5, 'd':1, 'b':7}
print(d)

# solution 1
tmp = sorted(d.items(), key=lambda n: n[1])
sort_d = dict(tmp)
print(sort_d)

#solution 2
dl = list(d.items())
dl.sort(key= lambda n:n[1], reverse=True)
sort_d = dict(dl)
print(sort_d)
