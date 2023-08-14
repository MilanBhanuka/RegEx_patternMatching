def traverse(Text, Pattern, breaking_point, pi):
    if breaking_point > len(Text) - len(Pattern):
        return False
    q = 0
    for i in range(len(Pattern)):
        if Text[i + breaking_point] != Pattern[i]:
            break
        q += 1
    if q == len(Pattern):
        return True
    if q == 0:
        return traverse(Text, Pattern, breaking_point + 1, pi)
    return traverse(Text, Pattern, breaking_point + (q - pi[q - 1][1]), pi)


def KMP(Text, Pattern):
    pi = []
    for i in range(len(Pattern) + 1):
        postfix = []
        prefix = []
        maxLength = 0
        sub = "".join(Pattern[: i])
        for j in range(1, i):
            prefix.append(sub[: j])
            postfix.append(sub[i - j:])
        for j in range(len(prefix)):
            if prefix[j] in postfix:
                if len(prefix[j]) > maxLength:
                    maxLength = len(prefix[j])
        if i != 0:
            pi.append([Pattern[i - 1], maxLength])
    return traverse(Text, Pattern, 0, pi)


def startWith(Text, Pattern):
    if KMP(Text[: len(Pattern) - 1], "".join(Pattern[1:])):
        return True
    else:
        return False


def endsWith(Text, Pattern):
    if KMP(Text[len(Text) - len(Pattern) + 1:], "".join(Pattern[0: len(Pattern) - 1])):
        return True and search(Text, "".join(Pattern[:len(Pattern) - 1]))
    else:
        return False


def start_with_and_ends_with(Text, Pattern):
    if KMP(Text, "".join(Pattern[1: len(Pattern) - 1])) and len(Text) == len(Pattern) - 2:
        return True
    else:
        return False


def search(Text, Pattern):
    if any(i == '|' for i in Pattern):
        return search(Text, Pattern.split('|')[0]) or search(Text, Pattern.split('|')[1])
    elif Pattern[0] == "^" and Pattern[-1] == "$":
        return start_with_and_ends_with(Text, Pattern)
    if Pattern[0] == "^":
        return startWith(Text, Pattern)
    elif Pattern[-1] == "$":
        return endsWith(Text, Pattern)
    return KMP(Text, Pattern)


if __name__ == '__main__':
    text = open("text.txt", 'r')
    pattern = open("pattern.txt", 'r')
    output = open("patternmatch.output", 'w')

    T = text.readline().strip()
    P = pattern.readline().strip()

    if search(T, P):
        output.writelines("Pattern is found")
    else:
        output.writelines("Pattern is not found")

    text.close()
    pattern.close()
    output.close()
