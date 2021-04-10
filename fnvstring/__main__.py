import sys
from fnvstring import hash

def compare():
    import timeit
    from fnvstring.hasher import Fvn64StringHasher
    def dohashlib(string:str):
        return str(int(hashlib.sha256(string.encode("utf-8")).hexdigest(), 16) % 10**11)
    print(f'compare fnvstring performance with hashlib')
    string = Fvn64StringHasher.random_string(length=128)
    salt = '_'
    times = 100000
    time_fnv = timeit.timeit(f"Fvn64StringHasher.as_bytes('{string}')", setup='from fnvstring.hasher import Fvn64StringHasher', number=times)
    print(f'fnv calculates {times} hash in {time_fnv}')
    cmd = f"hashlib.sha256('{string}'.encode('utf-8')).hexdigest()"
    time_sha256 = timeit.timeit(cmd, setup="import hashlib", number=times)
    print(f'sha256 calculates {times} hash in {time_sha256}')
    cmd_md5 = f"hashlib.md5('{string}'.encode('utf-8')).hexdigest()"
    time_md5 = timeit.timeit(cmd_md5, setup="import hashlib", number=times)
    print(f'md5 calculates {times} hash in {time_md5}')
    

def main() -> int:
    """Execute command line."""
    args = sys.argv
    command = args[0].split("/")[-1]
    countargs = len(args)

    USG_STR = (
        "Fowler–Noll–Vo hash generator\n\n"
        f"usage: {command} [-h] [-c] STRING [SALT]\n\n"
        "(C) 2020 David Vicente Ranz"
    )

    if not 2 <= countargs <= 3:
        print(USG_STR)
        return -1

    if args[1] == "-h":
        print(USG_STR)
        return 0

    if args[1] == "-c":
        compare()
        return 0

    string = args[1]
    salt = args[2] if len(args) == 3 else None

    print(hash(string, salt=salt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
