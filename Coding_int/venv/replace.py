

#Python challenge #1 Everybody thinks twice before solving this

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "


def replaceChars(input, c1, c2):
    # create lambda to replace c1 with c2, c2
    # with c1 and other will remain same
    # expression will be like "lambda x:
    # x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2"
    # and map it onto each character of string
    newChars = map(lambda x: x if (x != c1 and x != c2) else \
        c1 if (x == c2) else c2, input)

    # now join each character without space
    # to print resultant string
    print(''.join(newChars))


# Driver program
if __name__ == "__main__":
    print(message)
    input = message
    replaceChars(input, 'k', 'm')
    replaceChars(input, 'o', 'q')
    replaceChars(input, 'e', 'g')
    print(input)


