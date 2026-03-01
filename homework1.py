#1

# a = input('enter your name: ') 
# b = input('enter your surname: ')
# c = input('enter your age: ')

# def user_data(first_name,last_name,age):
#      print('Ism:', first_name )
#      print('Familiya:', last_name )
#      print('Yosh:', age )

# user_data(a,b,c)     

#2
# def find_max(a,b,c):
#     if a>b and a>c: print('Eng katta son - A =',a)
#     elif b>a and b>c: print('Eng katta son - B =',b)
#     elif c>a and c>b: print('Eng katta son - C =',c)
#     elif a==b and a>c:print('Eng katta son - A va B =',a)
#     elif a==c and a>b:print('Eng katta son - A va C =',a)
#     elif c==b and c>a:print('Eng katta son - C va B =',c)
#     elif a==b==c: print('Eng katta son - A va B va C =',a)
# a = int(input('enter first number: '))
# b = int(input('enter second number: '))
# c = int(input('enter third number: '))
# find_max(a,b,c)

#3

# def find_letter_count(word,letter):
#     word = word.lower()
#     letter = letter.lower()
#     s = 0
#     for i in word:
#         if i==letter:s+=1
#         else: continue
#     print(word,'sozida',letter,'dan', s,'ta')
# word = input('Enter any word: ')
# letter = input('Enter letter which you want find: ')

# find_letter_count(word,letter)

# 4

# def list_sum(myList):
#     s = 0
#     for i in myList: s+=1
#     print("Listning elementlar yig'indisi =",s)

# list_sum(['nums',10,2,5,'name',7,50,4,56,20,4])

# 5

# def daraja(a,b):
#     print(a**b)
# daraja(2,10)

# 6

# def daraja4(a,b,c,d):
#     print(a**b,c**d)

# daraja4(3,3,5,2)

# 7

# def digit_count_and_sum(word):
#     count = 0
#     sums = []
#     for i in word:
#         if i in '0123456789':
#             i = int(i)
#             count+=1
#             sums.append(i)
#         else: continue
#     print(count)
#     print(sum(sums))

# digit_count_and_sum('123456789iouer')

# 8

# def add_right(a,b):
#     print(str(a)+str(b))
# add_right(5,6)

# 9 

# def add_left(a,b):
#     print(str(b)+str(a))
# add_left(5,6)

# 10

# def work_with_list(a):
#     new_list = []
#     for i in a:
#       f = min(a)*i
#       new_list.append(f)
#     print(new_list)
# work_with_list([5,2,4,3,6,8,9])

# 11

# sales = {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
# def big_sales(sales):
#    return (max(sales,key = sales.get))
# print(big_sales(sales))

# 12

# def min_max(numbers,max_num,min_num):
#      if max(numbers)<=max_num and min(numbers)>=min_num:
#           print(max_num,'eng katta son')
#           print(min_num,'eng kichik  son')
#      else:
#           print(max_num,'eng katta son emas')
#           print(min_num,'eng kichik son emas')
          


         
# a =1,2,3,4,5,6,7,8,9,8,4,5,6
# b =9
# c =1
# min_max(a,b,c)

# 13 

products = [
  {
    "name": "Iphone X",
    "price": 600
  },
  {
    "name": "Iphone 12",
    "price": 1500
  },
  {
    "name": "Samsung Note 9",
    "price": 800
  },
  {
    "name": "Samsung S10",
    "price": 1100
  }
]
def expensiveProduct(products):
    print(max(products, key = lambda x:x['price']))


expensiveProduct(products)


# homework 2 

#1 set(add)
nums = {1,5,6,8,4,9,5}
nums.add(10)
nums.add('banana')
print(nums)

# clear() Method
nums.clear()
print(nums)

# copy() Method
y = nums.copy()
x = nums.copy()
print(y)

#difference() Method
nums = {1,5,6,8,4,9,5}
nums2 = {2,3,10,15,1}
z = nums.difference(nums2)
print(z)
a = {'apple','banana','pineapple'}
b = {'cherry','melon','banana'}
c = a.difference(b)
print(c)

#difference_update() Method
a = {'apple','banana','pineapple'}
b = {'cherry','melon','banana'}
a.difference_update(b)
print(a)
d = {'mouse','game','tower'}
e = {'game','hamburg','computer'}
d.difference_update(e)
print(d)

#discard() Method
e = {'game','hamburg','computer'}
e.discard('hamburg')
e.discard('game')
print(e)

#intersection() Method
a = {'apple','banana','pineapple'}
b = {'cherry','melon','banana'}
z= a.intersection(b)
print(z)
f = {'car','engine','ai'}
g = {'bread','car','phone'}
h = f.intersection(g)
print(h)

# intersection_update()Method
a = {'apple','banana','pineapple'}
b = {'cherry','melon','banana'}
a.intersection_update(b)
print(a)
f = {'car','engine','ai'}
g = {'bread','car','phone'}
f.intersection_update(g)
print(f)

#isdisjoint() Method
t = {'css','java','python'} 
w = {'c+','c','javascript'}
q = t.isdisjoint(w)
print(q)
d = {'mouse','game','tower'}
e = {'game','hamburg','computer'}
r = d.isdisjoint(e)
print(r)

#issubset() Method
a = {'glass','car', 'snow'}
s = {'insta','microsoft','hardware','glass','car', 'snow'}
m = a.issubset(s)
print(m)
t = {'css','java','python'} 
w = {'c+','c','javascript'}
b=t.issubset(w)
print(b) 

#issuperset() Method
j = {5,7,8}
l = {4,10,5,7,8,9,12}
z = l.issuperset(j)
print(z)
a = {1,2,3,4,5,6}
b = {2,3,4}
u = a.issuperset(b)
print(u)

#pop() Method
j = {5,7,8,10,15}
j.pop()
print(j)
a = {'glass','car', 'snow'}
a.pop()
print(a)

#remove() Method
t = {'css','java','python'} 
t.remove('css')
print(t)
e = {'game','hamburg','computer'}
e.remove('computer')
print(e)

#symmetric_difference() Method
a = {1,2,3,4,5,6}
b = {2,3,4}
pip = a.symmetric_difference(b)
print(pip)
d = {'mouse','game','tower'}
e = {'game','hamburg','computer'}
run = d.symmetric_difference(e)
print(run)

#symmetric_difference_update() Method
a = {1,2,3,4,5,6}
b = {2,3,4}
a.symmetric_difference_update(b)
print(a)
d = {'mouse','game','tower'}
e = {'game','hamburg','computer'}
d.symmetric_difference_update(e)
print(d)

#union() Method
num3 = {7,8,9,10}
num4 = {1,2,3,4,5}
num5 = num3.union(num4)
print(num5)
d = {'mouse','game','tower'}
e = {'game','hamburg','computer'}
p = d | e
print(p)

#update() Method
num3 = {7,8,9,10}
num4 = {1,2,3,4,5}
num3.update(num4)
print(num3)
a = {'apple','banana','pineapple'}
b = {'cherry','melon','banana'}
a.update(b)
print(a)
