def str2int(m):
    mb = ""
    for i in m:
        chi = ord(i)
        if len(str(chi)) < 3:
            schi = "0" + str(chi)
        else:
            schi = str(chi)
        mb = mb + schi
    mb = int(mb)
    print("Initial mb: ", mb)
    print("Initial m: ", m)
    return mb


def int2str(mb):
    m = ""
    if len(str(mb)) % 3 != 0:
        mb = "0" + str(mb)
    else:
        mb = str(mb)
    for j in range(int(len(mb)/3)):
        ch = ""
        for i in range(3):
            ch = ch + mb[j*3+i]
        m = m + chr(int(ch))
    print("Final mb: ", mb)
    print("Final m: ", m)
    return m


