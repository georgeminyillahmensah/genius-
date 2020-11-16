import hashlib
def hashing_method(password_to_hashed):
  hash1 = hashlib.md5(password_to_hashed)
  print("Your hashed password is: ", hash1.hexdigest())

def main():
  print("Password hashing script")
  password_to_hashed = raw_input("enter your password: ")
  hashing_method(password_to_hashed)

if __name__ == "__main__":
    main()