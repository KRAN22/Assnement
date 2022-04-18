def begin_end(func):
    def inner(*args):
        print("Welcome.....")
        func(*args)
        print("end......")
    return inner
