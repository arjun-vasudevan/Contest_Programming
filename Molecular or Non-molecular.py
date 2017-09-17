N = input()
good = "ClBrXeKrSiAsRnNeHeHCNOFPSI"

for i in range(N):
    i2 = raw_input()
    verdict = True
    for i in i2.split(" "):
        if i in good:
            verdict = True
            continue
        else:
            print "Not molecular!"
            verdict = False
            break
    if verdict == True:
        print "Molecular!"
