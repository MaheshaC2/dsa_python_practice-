# Problem: String Compression
# Category: Strings
# Time Complexity: O(n)
# Space Complexity: O(1)

def compress(chars):
    i = 0
    res = []

    while i < len(chars):
        char = chars[i]
        count = 0

        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1

        res.append(char)
        if count > 1:
            res.append(str(count))

    return "".join(res)
