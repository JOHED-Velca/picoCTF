f = open('dictionary.txt', 'r')
#i=0
while True:
    #if i == 5:
    #    continue
    val = (f.read(5).strip())
    print(val)
    if val == 'aaaa':
        print("found pw!")
        break
    #print(f.read(5).strip())
    #i += 1
else:
    print("no more passwords")

print("continue the code here <3")