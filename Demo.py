# for num in range(1,21):
# 	if(num == 4 or num == 13):
# 		print(f"{num}: is UNLUCKY") 
# 	elif (num % 2 == 0 ):
# 		print(f"{num}: is even")
# 	else:
# 		print(f"{num}: is odd")

# num = 1
# while( num < 5):
# 	print('\U0001f600' * num)
# 	num += 1
# i = 0
# while i <= 5:
#   i =+ 1
#   print(i)
# a = ['a','b','c','d']
# print(a)
# b = ''.join(st for st in a if st == 'd')
# print(b)

# ... Dirctionary .... #
# a = {"a":'a'}
# # print(a)
# a = dict.fromkeys(['name','email','phone','sex','addr','pin'],'NAN')
# answer = {}.fromkeys('aeiou', 0)
# print(answer)
# # b =  dict(a=1,b=2)
# # print(b)
# clone = a.copy()
# a.clear();
# # a['name'] will throught an error.
# print(a.get('name'), clone)
# clone.pop('name')
# # clone.popitem() will remove randomly
# clone.update({'cloned': 'Item 1'})
# print(clone)
# playlist = {
# 	'title': 'patagonia bus',
# 	'author': 'colt steele',
# 	'songs': [
# 		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
# 		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
# 		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
# 	]
# }

# total_length = 0
# for song in playlist['songs']:
# 	total_length += song['duration']
# print(total_length)

# ... Dirctionary Comparision.... #
instructor = {'name': 'mohan', 'city': 'Banglore'}
# Instructor = {k.upper(): v.upper() for k,v in instructor.items()}
# print(Instructor)
instructor = {k: ( v.upper() if v is 'mohan' else v ) for k,v in  instructor.items()}
print(instructor)
# a = [1,2,3,4,5]
# b = {num:('even' if num % 2 == 0 else "odd") for num in a}
# print(b)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = { list1[i]: list2[i] for i in range(0,3)}
# print(answer)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# print(dict(zip(list1, list2)))

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = dict(person)
# print(answer)
# print({ k:v for k,v in person} )

# answer = {count: chr(count) for count in range(65, 91)}
# print(answer)