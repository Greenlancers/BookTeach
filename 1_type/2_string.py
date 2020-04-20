print("=============================================================================")
print("String")
print()


S = 'Spam'
SS = "Superman"
line = 'aaaa,dddd,ffff,vvvvv'
print ("Srting S", S)
print ("String SS",SS)
print ("String line", line)
print("len(S)",len(S))
print("SS substring:",SS[0:5])
print ("SS[-3:]",SS[-3:])  # [: - first symbol
print ("SS[5:8]",SS[5:8])	 # :] - last symbol
print ("line[0:15:3]",line[0:15:3] )  # substring from 0 to 15 each third element
print ("S[::-1]",S[::-1]) 	# reverse string each element(or -2(second) -3(third))
print ("SS[5]",SS[5])
print ("S + SS concatination",S+SS)

print ("'man' index", SS.find("man"))
print ("SS replace",SS.replace('man','woman'))
print ("line split",line.split(','))

for i in SS: print (i,end =' ')
print()
print('k' in SS)
#print(dir(S))
#print (help(S.replace))

STRING = """fgsdfgsdfgsdfgsd""fgsd'fgsdfg'sd'fg'sdfg's'dfg;d"""
print ("ord('s')",ord('s')) # return ASCII number of char
print ("char(116)",chr(116)) # return Char from ASCII number


path = r"c:\new\test\yo.txt"  #r"" or R"" -without masking symbols in ""
s = "s\tp\na\x00m \v 0x4f"
print(s)

print("That is %d %s bird!" % (2,"dead"))
print ("That is {count} {0} bird!".format("dead", count=2))
print("{0:>011,.5f}".format(2573673.12346245) ) #first element: to right end>(< left)0(with right) 11 symbol split , by each 3 .float 5 symbol after point
print(format(5.677899, ".2f"))


s = "spammy"
L = list(s)  #convert string to LIST
print(L)
L[3] = 'x'
L[4] = 'x'
s = ''.join(L) #convert List to string
print (s)
print ('XXX'.join(['aaa','bbb','ccc','fff'])) # .join unate strings whith separator

print(vars()) # vars() return all existing variables as name:value

print("%(s)s eat %(SS)s" % vars()) ## get value by name from vars()



