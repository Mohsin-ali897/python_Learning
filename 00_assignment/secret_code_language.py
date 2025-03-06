st = input('enter your message:')
# print(st)
words = st.split(' ')
# print(words)
coding = True
if (coding):
    for word in words:    
        nword = []
        if(len(words)>= 3):
            r1 = 'dfd'
            r2 = 'fgt'
            newStr = r2 + word[1:] + word[0] + r1
            nword.append(newStr)
            print(''.join(nword))
            # print(nword)
        else:
            nword.append(word[::-1])
            print(nword)
else:
    for word in words:
        if(len(word) >= 3):
            nword = []
            str = word[3:-3]
            str = str[1] + str[0]
            nword.append(str)
            print(nword)
        else:
            word[::-3]
            print(word)
    
# my name is mohsin  