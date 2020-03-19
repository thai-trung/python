# implement command-line arguments in python

from sys import argv, exit

if len(argv) != 2 :
    print("Missing command-line arguments!")
    exit(1)

print(f"Hello, {argv[1]}")
exit(0)