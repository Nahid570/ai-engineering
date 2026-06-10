
# i = 0

# while i < 3:
#     print("Meow")
#     i += 1

# for i in range(3):
#     print("Meow: ", i + 1)

# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

def main():
    n = get_number()
    meow(n)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()