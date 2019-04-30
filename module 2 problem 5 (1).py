# Jamaree Jackson
#04/21/19

#problem 5 this wrtes a program that counts the number of times a letter pops up

a ="a,b,c,d,e,f,g, dreamville,boat"

b = {}
for x in 'abcdefgehibfhjskbgrdryohd':
    b[x] = 0
    for letter in a:
        if letter in b:
            b[letter] += 1
            print(b)
