def check_os(opssystem):
     if opssystem=='Windows':
        print("The operating system is Windows.")
     elif opssystem=='Linux':
        print("The operating system is Linux.")
     else:
        print("The operating system is not recognized.")

for i in range(1,5):
      print("Iteration:", i)

import os
print(os.uname().sysname)
