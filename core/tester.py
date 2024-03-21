import bluetooth_utils

test = "hello"
test_encoded = bluetooth_utils.byteArrayToHexString(bytes(test, 'ascii'))
print(test_encoded)

byte_val = b'\n\x01'
int_val = int.from_bytes(byte_val, "little")
print(int_val)

a = [10,1]
b = bytearray(a)
i = int.from_bytes(b, "little")
print(i)

def encode_content(content):
    encoded = None
    content_list = str(content).split(',')
    try:
        for c in content_list:
            encoded.append(int(c))
        encoded = bytearray(encoded)
    except:
        encoded = bytes(content, 'ascii')
    finally:
        return encoded
        

test = "10,1"
test2 = "hello"
encoded = encode_content(test)
print(encoded)
encoded2 = encode_content(test2)
print(encoded2)