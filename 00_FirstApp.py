

a=2
c=a * 2
if a == c: 
    b = 3
else:
    b = 0
print("b = {}".format(b) , end=" " )

"""
OUTPUT
___________________________
a= 5 b = 1 Hello
"""



"""--------------- loop -----------------"""

counter=0

while counter<10:
    print("in loop",counter)
    counter= counter+1
    #counter+=1
    #counter++ (invaild syntax in python)
else:
    print("after loop",counter)

print("end of program")
"""
OUTPUT
___________________________
in loop 0
in loop 1
in loop 2
in loop 3
in loop 4
in loop 5
in loop 6
in loop 7
in loop 8
in loop 9
after loop 10
end of program
"""
name="Bob and Alice"

print("name.startswith(\"Bo\")")
print(name.startswith("Bo"))
print("------------------------")


print("name.startswith(\"Alice\")")
print(name.startswith("Alice"))
print("------------------------")

print("name.endswith(\"Alice\")")
print(name.endswith("Alice"))
print("------------------------")


print("\"or\" in name")
print("or" in name)
print("------------------------")

print("\"and\" in name")
print("and" in name)
print("------------------------")

print("name[2]")
print(name[2])
print("------------------------")

MyList=['Apple', 'Banan', 'Melon', 'Mango']
print(MyList)
j=len(MyList)
for x in range(len(MyList)):
    print(MyList)
    del MyList[0]
    print(MyList)