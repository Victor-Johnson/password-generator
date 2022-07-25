import random
print("Your Password is : ",end=" ")
ucount = 3
scount = 3
sum_count = ucount + scount
uword = random.sample(range(65,90),ucount)
sword = random.sample(range(97,122),scount)
num1 = random.randint(48,57)
num2 = random.randint(48,57)
spword = ['@','#','$','*','&','?','~','/','!','%','^','-']
npword1 = chr(num1)
npword2 = chr(num2)
letter_count = uword + sword
random.shuffle(letter_count)
for x in letter_count :
  print(chr(x),end ='')

print(npword2,npword1,random.choice(spword))


