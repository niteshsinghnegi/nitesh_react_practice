# Secret code: very simple version

choice = input("Enter choice (code/decode): ").strip().lower()
msg = input("Enter your message: ").split()

newmsg = []

if choice == "code":
    for word in msg:
        if len(word) >= 3:
            # move first letter to end, then add fixed 3+3 chars
            word = "sgf" + word[1:] + word[0] + "hjk"
        else:
            # words of length < 3 are reversed
            word = word[::-1]
        newmsg.append(word)
    print("Encoded:", " ".join(newmsg))

elif choice == "decode":
    for word in msg:
        if len(word) < 3:
            word = word[::-1]
        else:
            # remove 3 chars from start & end, then move last to front
            if len(word) >= 3:      # safety: "sgf" + at least 1 + "hjk"
                word = word[3:-3]
                word = word[-1] + word[:-1]
        newmsg.append(word)
    print("Decoded:", " ".join(newmsg))

else:
    print("Invalid choice!")
