# sets and dictionary
# Dictionaries are mutable, unordered collections of key-value pairs.
# Sets are unordered collections of unique elements.
# They are mutable, but they do not support indexing or slicing.
# Dictionaries
dict = {
  "name": "Rabin",
  "age": 22,
  "is_student": True,
  "marks": [11, 22, 33, 44],
  "topic": ("python", "java", "c++")
}
# print(dict) 
# print(dict["is_student"]) 
# print(dict["age"]) 
# print(type(dict)) 

dict["name"] = "Nanu"
dict["TYPE"] = 23
# print(dict)

null_dict= {}
# print(null_dict)

# Nested dictionary
nested_dict = {
  "dict1": {
    "name": "Rabin",
    "age": 22,
    "is_student": True,
    "marks": [11, 22, 33, 44],
    "topic": ("python", "java", "c++")
  },
  "dict2": {
    "name": "Nanu",
    "age": 23,
    "is_student": False,
    "marks": [12, 23, 34, 45],
    "topic": ("python", "java", "c++")
  }
}
# print(nested_dict)
# print(nested_dict["dict1"]["name"])

# print(list(nested_dict.keys()))
# print(len(list(nested_dict.keys())))
# print(len(nested_dict))
# print(nested_dict.values())
# print(list(nested_dict.values()))
# print((nested_dict.items()))
# print(list(nested_dict.items()))

# print(nested_dict["dict1"]["name"])
# print(nested_dict.get("dict1"))

nested_dict.update({"dict3": {
  "name": "Pradip",
  "age": 23,
  "is_student": False,
  "marks": [12, 23, 34, 45],
  "topic": ("python", "java", "c++")
}})

# print(nested_dict)

# Sets in Python
# Sets are unordered collections of unique elements.
# They are mutable, but they do not support indexing or slicing.
# Sets are created using curly braces {} or the set() constructor.

# collection = {1, 2, 3, 4, 5}
# print(type(collection))
# print(collection)
# print(len(collection))

collection = set()
# print(type(collection))
collection.add(1)
collection.add("rabin")
collection.add(3)
collection.add(4)
collection.add((1, 2, 3))
# collection.remove(3)
# collection.pop()
# collection.clear()
# print(collection)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))
print(set1.intersection(set2))
