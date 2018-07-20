jog1 = raw_input()
jog2 = raw_input()

r = "R"
s = "S"
p = "P"

if jog1 == jog2:
    print("empate")
elif jog1 == r and jog2 == s:
    print("jog1")
elif jog1 == p and jog2 == r:
    print("jog1")
elif jog1 == s and jog2 == p:
    print("jog1")
elif jog2 == r and jog1 == s:
    print("jog2")
elif jog2 == p and jog1 == r:
    print("jog2")
elif jog2 == s and jog1 == p:
    print("jog2")