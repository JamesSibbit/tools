import hashlib
import getpass

# print(hashlib.algorithms_available)

hash_obj = hashlib.sha3_256()
hash_obj_two = hashlib.sha3_256()

hash_obj.update(b'Hi Luca')
hash_obj_two.update(b'Hi luca')

print(hash_obj.hexdigest())
print(hash_obj_two.hexdigest())


def get_pass():
    password = getpass.getpass('Set password: ')
    hash_pass = hashlib.sha3_256()
    hash_pass.update(password.encode())
    return hash_pass

def pass_check():
    hash_pass = get_pass()
    for retry in range(5):
        password_check = getpass.getpass('What\'s your password?: ')
        hash_pass_check = hashlib.sha3_256()
        hash_pass_check.update(password_check.encode())
        if hash_pass_check.hexdigest() == hash_pass.hexdigest():
            print('Correct pass!')
            break
        print('Try Again')
    else:
        print('Too many tries')
        sys.exit(1)

pass_check()
