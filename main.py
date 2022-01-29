f=open("text.txt")
fileLines=f.readlines()
for line in fileLines:
    print(line)
introstring ="my name is amruthaa. i am in the 9th grade"
words=introstring.split(".")
print(words)
def greet(name):
    print("hello "+name)
greet("john")
