def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("done running function")
    return wrapper

@announce
def hello():
    print("Hello, World")

hello()