list = ["Test", "Test1", "Test2", "Test3", "Test4"]
word = "LastTest"

list.append("AnotherTest")
list.append("AnotherTest1")
list.append("LastTest")

list.remove("AnotherTest")

if word in list:
    print(word + " Is in the list")
else:
    print(word + " Is not in the list")


for acronym in list:
    print(acronym)