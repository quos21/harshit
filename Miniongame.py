vowel=["A","E","I","O","U"]
consonants=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
b=input("")
l_string=len(b)
list_string=[]
vowel_list=[]
consonant_list=[]
for i in range(l_string):
    c=b[i]
    list_string.append(c)
range_string=1
main=0
while main<l_string:
    while range_string<=l_string:
        temp = "".join(list_string[main:range_string])
        if (list_string[main] in vowel):
            vowel_list.append(temp)
        elif (list_string[main] in consonants):
            consonant_list.append(temp)
        range_string+=1
    main+=1
    range_string=2
l_vowel=len(vowel_list)
vowel_list2=[]
for i in range(l_vowel):
    if vowel_list[i]!="":
        vowel_list2.append(vowel_list[i])
#print(vowel_list2)
l_consonants=len(consonant_list)
consonant_list2=[]
for i in range(l_consonants):
    if consonant_list[i]!="":
        consonant_list2.append(consonant_list[i])
print(consonant_list2)
consonant_win=len(consonant_list2)
vowel_win=len(vowel_list2)
if vowel_win>consonant_win:
    print("Kevin",vowel_win)
elif vowel_win==consonant_win:
    print("Draw")
else:
    print("Stuart",consonant_win)
