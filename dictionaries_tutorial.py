foods = ["pizza", "pasta", "burger", "sushi", "steak"]
foods.append("ice cream")
del foods[1]
print(foods)


friends_colors = {"Alice": "blue", "Bob": "green", "Charlie": "red"}
friends_colors["Dave"] = "purple"
friends_colors["Alice"] = "pink"
print(friends_colors)


# list.append(x)
# 在列表末尾添加一个元素，相当于 a[len(a):] = [x] 。

# list.extend(iterable)
# 用可迭代对象的元素扩展列表。相当于 a[len(a):] = iterable 。

# list.insert(i, x)
# 在指定位置插入元素。第一个参数是插入元素的索引，因此，a.insert(0, x) 在列表开头插入元素， a.insert(len(a), x) 等同于 a.append(x) 。

# list.remove(x)
# 从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。

# list.pop([i])
# 删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，a.pop() 删除并返回列表的最后一个元素。（方法签名中 i 两边的方括号表示该参数是可选的，不是要求输入方括号。这种表示法常见于 Python 参考库）。

# list.clear()
# 删除列表里的所有元素，相当于 del a[:] 。

# list.index(x[, start[, end]])
# 返回列表中第一个值为 x 的元素的零基索引。未找到指定元素时，触发 ValueError 异常。

# 可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

# list.count(x)
# 返回列表中元素 x 出现的次数。

# list.sort(*, key=None, reverse=False)
# 就地排序列表中的元素（要了解自定义排序参数，详见 sorted()）。

# list.reverse()
# 翻转列表中的元素。

# list.copy()
# 返回列表的浅拷贝。相当于 a[:] 。

# 2
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

# 0
fruits.count('tangerine')

# 3
fruits.index('banana')


fruits.reverse()
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']


fruits.append('grape')
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']


fruits.sort()
fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
# 'pear'







tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
# 4098
del tel['sape']
tel['irv'] = 4127
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
# ['jack', 'guido', 'irv']
sorted(tel)
# ['guido', 'irv', 'jack']
'guido' in tel
# True
'jack' not in tel
# False


# dict() 构造函数可以直接用键值对序列创建字典：

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'guido': 4127, 'jack': 4098}


# 字典推导式可以用任意键值表达式创建字典：

{x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}


# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷：

dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}







stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
# [3, 4, 5, 6, 7]

stack.pop()
# 7

stack
# [3, 4, 5, 6]

stack.pop()
# 6

stack.pop()
# 5

stack
# [3, 4]





stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack



from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
queue.popleft()                 # The second to arrive now leaves
# 'John'
queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])


squares = []
for x in range(10):
    squares.append(x**2)

squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




