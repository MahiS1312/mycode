def greet(name):
    return f"Hello, {name}! Welcome to Jenkins CI/CD Demo."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))