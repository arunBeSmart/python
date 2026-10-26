a = 10
b = 25
if a >10:
    print("A is bigger")
    print("difference is ",a-b)
else:
    print("B is bigger")
    print("difference is ",b-a)

env="test"
if env=="dev":
    print("Development Environment")
elif env=="test":
    print("Testing Environment")
else:
    print("Production Environment")