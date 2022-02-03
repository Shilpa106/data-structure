# from collections import namedtuple

# # declaring namedtuple()
# Student=namedtuple('Student',['name','age','DOB'])

# # Adding values
# S=Student("Shi",'11','1234444')

# # Access using index
# print("The student age using index is:", end="")
# print(S[1])

# # access using name
# print("The Student name using keyname is: ", end="")
# print(S.name)


# # Access by name, index and getattr()

# import collections

# # Declaring namedtuple()
# Student=collections.namedtuple('Student',['name','age','DOB'])

# # Adding values
# S=Student('Shya','33','1324256')

# # Access using index
# print("The Student age using index is: ", end="")
# print(S[1])

# # Access using name
# print("The Student name using keyname is:", end="")
# print(S.name)

# # Access using getattr()
# print("The Student DOB using getattr() is:", end="")
# print(getattr(S,'DOB'))

# # Conversion operations

# from collections import namedtuple


# # _make():used to return a namedtuple() from the iterable passed as arg
# # _asdict():returns the OrderedDict() as the mapped values of namedtuple()

# # using "**" operator: this function is used to convert a dictionary into the namedtuple()

# import collections

# # Declaring namedtuple()
# Student=collections.namedtuple('Student', ['name','age','DOB'])

# # Adding values
# S=Student('Ram','33','342222')

# # initializing iterable
# li=['shyam','12','1829999']

# # initializing dict
# di={'name':"rakshi",'age':12, 'DOB':'1234567'}

# # using _make() to return namedtuple()
# print("The namedtuple instance using iterable is : ")
# print(Student._make(li))

# # using _asdict() to return an OrderedDict()
# print("The OrderedDict instance using namedtuple is :")
# print(S._asdict())

# # using ** operator to return namedtuple from dictionary
# print("The namedtuple instance from dict is : ")
# print(Student(**di))


# # M3
# import collections

# # declaring namedtuple()
# Student=collections.namedtuple('Student',['name','age','DOB'])

# # Adding values
# S=Student('Ra','11','1211111')

# # using _fields to display all the keynames of  namedtuple()
# print("All the fields of students are")
# print(S._fields)

# # ._replace returns a new namedtuple, it does not modify the original
# print("returns a new namedtuple:")

# print(S._replace(name='MAn'))

# # original namedtuple
# print(S)


# M4
