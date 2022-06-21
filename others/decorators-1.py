# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}
# print(user1.get("valid"))

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"] == True:
            fn(*args, **kwargs)    
        else:
            print(f"Access denied")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)