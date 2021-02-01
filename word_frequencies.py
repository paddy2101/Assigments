fileName = input("Enter File Name : ")
f=open(fileName,"r")
fileData = f.read();
words=fileData.split(" ")
freq={}
for i in words:
    if(i not in freq):
        freq[i]=0
    else:
        freq[i]+=1
    
word = input("Enter Word to know Its frequeny : ")
if freq.get(word) == None:
    print("{} is not in file".format(word))
else:
    print('Frequency of "{}" is {}'.format(word, freq.get(word))) 

