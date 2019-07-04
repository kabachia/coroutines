#Program to demonstrate coroutine execution
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

#Calling coroutine, nothing will happen
corou = print_name("Dear")

corou.__next__()

corou.send("Atul")
corou.send("Dear Atul")
