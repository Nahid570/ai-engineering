name = input("What's your name? ")

match name:
    case "Alice" | "Bob":
        print(f"Hello, {name}!")
    case _:
        print("Hello, stranger!")