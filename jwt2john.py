import sys
from jwt.utils import base64url_decode
from binascii import hexlify


def jwt2john(jwt):
    """
    Converts the signature from base64 to hex, and seperates it from the data with a #
    allowing John to parse it.
    :param jwt: JWT string to johnify
    :return: johnified JWT string
    """
    jwt_bytes = jwt
    parts = jwt_bytes.split('.')

    data = parts[0] + '.' + parts[1]
    signature = hexlify(base64url_decode(parts[2]))
    return f"{data}#{signature.decode('utf-8')}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} JWT_STRING")
    else:
        john = jwt2john(sys.argv[1])
        print(john)
