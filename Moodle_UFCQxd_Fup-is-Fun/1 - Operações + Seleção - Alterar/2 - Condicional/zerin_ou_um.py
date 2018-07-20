jog1 = raw_input()
jog2 = raw_input()
jog3 = raw_input()

if jog1 == jog2 and jog2 == jog3:
    print("empate")
elif jog1 == jog2 and jog2 != jog3:
    print("jog3")
elif jog1 != jog2 and jog2 == jog3:
    print("jog1")
elif jog1 == jog3 and jog2 != jog3:
    print("jog2")