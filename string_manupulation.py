'''
1.	Create a string “Grow Gratitude”.
Code for the following tasks:
a)	How do you access the letter “G” of “Grow”?
b)	How do you find the length of the string?
c)	Count how many times “G” is in the string?

'''

s = 'Grow Gratitude'

print(s[0]) # capturing 'G' from 'Grow'
print(len(s)) # capturing length of string s
print(s.count('G')) # counting 'G' from the string s

'''

2.	Create a string “Being aware of a single shortcoming within yourself is far more useful than 
    being aware of a thousand in someone else.”
Code for the following:
a)	Count the number of characters in the string.

'''
s1 = 'Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.'
print(len(s1)) # counting the all charecters



'''
3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
Code for the following tasks:
a)	get one char of the word
b)	get the first three char
c)	get the last three char
'''

s2 = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

s3 = s2.split(' ')

one_char = [i[0] for i in s3]
print(one_char)  # get one char of the word


print(s2[:3:]) # get the first three char

print(s2[-3::1]) # get the last three char


'''
4.	create a string "stay positive and optimistic". Now write a code to split on whitespace.
Write a code to find if:
a)	The string starts with “H”
b)	The string ends with “d”
c)	The string ends with “c”
    
'''
t = "stay positive and optimistic"

s_split = t.split()

print('starts with H : ', t.startswith('H'))
print('ends with d : ', t.endswith('d'))
print('ends with c : ', t.endswith('c'))



'''

5.	Write a code to print " 🪐 " one hundred and eight times.

'''

for i in range(109):
    print(" 🪐 ", end = ' ')
    
'''
6.	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”

'''

g = 'Grow Gratitude'
print(g.replace('Grow','Growth of'))


'''
7.	A story was printed in a pdf, which isn’t making any sense. i.e.:
“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,
nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef 
a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ 
.eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT 
.nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”

You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in the correct 
order.

'''
word = '.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A'
print(word[::-1])
