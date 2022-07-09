from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password, hashed_password) -> bool:
    return pwd_context.verify(password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


if __name__ == '__main__':
    pw = '123456'
    pw2 = '1234567'
    hash_pw = hash_password(pw)
    hash_pw2 = hash_password(pw2)

    print(hash_pw, pw, verify_password(pw, hash_pw))
    print(hash_pw2, pw2, verify_password(pw2, hash_pw2))
    print(verify_password(pw2, hash_pw))
    print(verify_password(pw, hash_pw2))
    print(type(hash_pw), type(hash_pw2))