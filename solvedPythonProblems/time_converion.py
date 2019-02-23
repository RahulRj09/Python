def timeConversion(s):
    if "P" in s:
        s = s.split(":")
        if s[0] == '12':
            s = s.split(":")
            s[2] = s[2][:2]
            print(":".join(s))
        else:
            s[0] = str(int(s[0])+12)
            s[2] = s[2][:2]
            print(":".join(s))
    else:
        s = s.split(":")
        if s[0] == "12":
            s[0] == "00"
            print(s)
            s[2] = s[2][:2]
            print(":".join(s),'AM')
        else:
            s[2] = s[2][:2]
            print(":".join(s))
s = input()
timeConversion(s)


