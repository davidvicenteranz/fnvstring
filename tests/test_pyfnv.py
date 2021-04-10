from fnvstring import Fvn64SaltedHasher, Hash, hash, random
from fnvstring.hasher import Fvn64StringHasher


def test_ok():
    assert Hash.works_ok() is True


def test_Salted():
    salted = Fvn64SaltedHasher("mysalt")
    assert salted.salt == "mysalt"
    assert salted.hash("A") == Hash.from_string("A", "mysalt")
    assert salted.hash("A") != Hash.from_string("A")
    assert hash('A', '') == 'nrcBhky9Y68'


def test_collision():
    millions = 1
    data = {}
    
    [data.setdefault(string, None) for string in set([Fvn64StringHasher.random_string() for i in range(0, int(millions*1000000))])]
    
    strings = list(data.keys())
    
    len(strings)/1000000 == millions
    
    salt = '$'
    
    for i in range(0, len(strings)):
        string = strings[i]
        hashed = hash(string)
        salted = hash(string, salt=salt)
        assert data.setdefault(hashed, None) == None
        assert data.setdefault(salted, None) == None
    
    now_strings = list(data.keys())

    assert len(now_strings) == len(strings) * 3
