# for i in range(10):
#     print (i+1) 
############################# 

# for i in range(2,11,2):
#     print (i)
#############################

# sum=0
# for i in range(1,8,2):
#     sum += i
# print(sum)
#############################

# for i in range(10,0,-1):
#     print (i)
#############################

# for i in range(4,21,4):
#     print (i)
#############################

# product=1
# for i in range(1,6):
#     product*=i
# print(product)
#############################

# for i in range(3,13):
#     if i % 3 == 0:
#         print (i)
#############################

# for i in range (5,0,-1):
#     print(i)
# print("Blast Off!")
#############################

# for i in range(1,6):
#     print(i*i)

# for n in range(1,8):
#     product=1
#     for i in range(n,0,-1):
#         product*=i
#     print(product)
#############################

# str= "Wonderful"
# result = ""
# for i in range(1,len(str),2):
#     result += (str[i])
# print(result)
#############################

# count=0
# str="computer"
# for i in range(1,len(str)):
#     if str[i] in ["a","e","i","o","u"]:
#         count+=1
# print(count)
#############################

backwards=""
forwards="racecar"

for i in range(len(forwards)-1,-1, -1):
    backwards+=forwards[i]

if backwards == forwards:
    print("Yes its a palindrome")
else:
    print ("No palindrome")
    