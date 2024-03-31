jahr = int(input())

if jahr % 4 == 0:
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            print("Schaltjahr")
        else:
            print("Kein Schaltjahr")
    else:
        print("Schaltjahr")
else:
    print("Kein Schaltjahr")
