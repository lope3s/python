from hashlib import md5

if __name__ == "__main__":
    key = "iwrupvqb"
    positive_integer = 0
    while True:
        md5_hash = md5()
        # string formating options
        data = f'{key}{positive_integer}'
        # data conversion to bytes
        md5_hash.update(bytearray(data, 'utf-8'))
        hash = md5_hash.hexdigest()
        # string methods
        if hash.startswith("000000"):
            print(hash, positive_integer)
            break
        positive_integer += 1
