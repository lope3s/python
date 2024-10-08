class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

# prints: B, C, D
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# prints: B, B, B, why?
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
