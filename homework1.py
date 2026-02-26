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