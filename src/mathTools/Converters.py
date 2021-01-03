# Those converters are made to get an int value of 3-digit number
# from any alphanumeric character
# based in unicode table and to undo this process
# (from 3-digit number to a alphanumeric char)
# Every 3 digit group belongs to a char in unicode
def str2int(m):
    mb = ""
    for i in m:
        chi = str(ord(i))
        if len(chi) < 3:  # For the char which code is lower then 3 digits, a "0" is added
            schi = "0" + chi
        else:
            schi = chi
        mb = mb + schi
    mb = int(mb)
    print("Initial mb: ", mb)
    print("Initial m: ", m)
    return mb


def int2str(mb):
    m = ""
    if len(str(mb)) % 3 != 0:
        mb = "0" + str(mb)  # In case the first char code has 2 digits instead of 3,
        # the total length of the code will not be divider of 3
        # Ex: "a" = "097" -> int("097") = 97 -> It's needed to add a "0" to get back "097"

    else:
        mb = str(mb)
    for j in range(int(len(mb) / 3)):  # This loop gets every single character from the int code
        ch = ""
        for i in range(3):
            ch = ch + mb[j * 3 + i]
        m = m + chr(int(ch))
    print("Final mb: ", mb)
    print("Final m: ", m)
    return m
